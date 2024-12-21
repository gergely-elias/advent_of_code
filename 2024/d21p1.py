import enum
import fileinput
import itertools
import networkx

input_lines = list(fileinput.input())
codes = [line.strip() for line in input_lines]


class KeypadType(enum.Enum):
    NUMERIC = enum.auto()
    DIRECTIONAL = enum.auto()


keypad_layouts = {
    KeypadType.NUMERIC: ["789", "456", "123", " 0A"],
    KeypadType.DIRECTIONAL: [" ^A", "<v>"],
}

direction_button_mapping = {
    (1, 0): "v",
    (0, 1): ">",
    (-1, 0): "^",
    (0, -1): "<",
}

robot_count = 2

key_coords = {}
for keypad_type in list(KeypadType):
    keypad_layout = keypad_layouts[keypad_type]
    key_coords[keypad_type] = {
        keypad_layout[y][x]: (y, x)
        for y in range(len(keypad_layout))
        for x in range(len(keypad_layout[y]))
        if keypad_layout[y][x] != " "
    }

keypad_graphs = {}
for keypad_type in list(KeypadType):
    keypad_layout = keypad_layouts[keypad_type]
    keypad_graph = networkx.Graph()
    for y in range(len(keypad_layout)):
        for x in range(len(keypad_layout[y])):
            if y > 0 and keypad_layout[y][x] != " " and keypad_layout[y - 1][x] != " ":
                keypad_graph.add_edge((y, x), (y - 1, x))
            if x > 0 and keypad_layout[y][x] != " " and keypad_layout[y][x - 1] != " ":
                keypad_graph.add_edge((y, x), (y, x - 1))
    keypad_graphs[keypad_type] = keypad_graph


def tuple_diff(minuend, subtrahend):
    return tuple(
        minuend_coord - subtrahend_coord
        for minuend_coord, subtrahend_coord in zip(minuend, subtrahend)
    )


def transfrom_path_into_word(path):
    return "".join(
        direction_button_mapping[tuple_diff(*step)] for step in zip(path[1:], path[:-1])
    )


def generate_next_layer_words(word, keypad_type):
    key_coords_to_push = [
        key_coords[keypad_type][letter] for letter in list("A" + word)
    ]
    word_segment_alternatives_sequence = []
    for key_positions_from_and_to in zip(
        key_coords_to_push[:-1], key_coords_to_push[1:]
    ):
        word_segment_alternatives = [
            transfrom_path_into_word(path) + "A"
            for path in networkx.all_shortest_paths(
                keypad_graphs[keypad_type], *key_positions_from_and_to
            )
        ]
        word_segment_alternatives_sequence.append(word_segment_alternatives)
    return list(
        "".join(word_segments)
        for word_segments in itertools.product(*word_segment_alternatives_sequence)
    )


total_complexity = 0
for code in codes:
    code_value = int(code[:-1])
    all_next_layer_words = generate_next_layer_words(code, KeypadType.NUMERIC)

    for layer in range(robot_count):
        all_words = all_next_layer_words
        all_next_layer_words = []
        for word in all_words:
            all_next_layer_words.extend(
                generate_next_layer_words(word, KeypadType.DIRECTIONAL)
            )
    total_complexity += code_value * min([len(word) for word in all_next_layer_words])
print(total_complexity)
