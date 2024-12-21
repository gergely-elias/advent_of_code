import enum
import fileinput
import itertools
import networkx

input_lines = list(fileinput.input())
codes = [line.strip() for line in input_lines]


class KeypadType(enum.Enum):
    NUMERIC = enum.auto()
    DIRECTIONAL = enum.auto()


keypadlayouts = {
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
for keypadtype in list(KeypadType):
    keypadlayout = keypadlayouts[keypadtype]
    key_coords[keypadtype] = {
        keypadlayout[y][x]: (y, x)
        for y in range(len(keypadlayout))
        for x in range(len(keypadlayout[y]))
        if keypadlayout[y][x] != " "
    }

keypadgraphs = {}
for keypadtype in list(KeypadType):
    keypadlayout = keypadlayouts[keypadtype]
    keypadgraph = networkx.Graph()
    for y in range(len(keypadlayout)):
        for x in range(len(keypadlayout[y])):
            if y > 0 and keypadlayout[y][x] != " " and keypadlayout[y - 1][x] != " ":
                keypadgraph.add_edge((y, x), (y - 1, x))
            if x > 0 and keypadlayout[y][x] != " " and keypadlayout[y][x - 1] != " ":
                keypadgraph.add_edge((y, x), (y, x - 1))
    keypadgraphs[keypadtype] = keypadgraph


def tuple_diff(minuend, subtrahend):
    return tuple(
        minuend_coord - subtrahend_coord
        for minuend_coord, subtrahend_coord in zip(minuend, subtrahend)
    )


def transfrom_path_into_word(path):
    return "".join(
        direction_button_mapping[tuple_diff(*step)] for step in zip(path[1:], path[:-1])
    )


def generate_next_layer_words(word, keypadtype):
    key_coords_to_push = [key_coords[keypadtype][letter] for letter in list("A" + word)]
    word_segment_alternatives_sequence = []
    for key_positions_from_and_to in zip(
        key_coords_to_push[:-1], key_coords_to_push[1:]
    ):
        word_segment_alternatives = [
            transfrom_path_into_word(path) + "A"
            for path in networkx.all_shortest_paths(
                keypadgraphs[keypadtype], *key_positions_from_and_to
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
