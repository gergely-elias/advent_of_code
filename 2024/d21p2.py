import enum
import fileinput
import functools
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

robot_count = 25

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


def word_cost(keypadtype, word, layer):
    return sum(
        key_cost(*keypair, keypadtype, layer) for keypair in zip("A" + word[:-1], word)
    )


@functools.cache
def key_cost(key_from, key_to, keypadtype, layer):
    if layer == robot_count + 1:
        return 1
    key_positions_from_and_to = [
        key_coords[keypadtype][key] for key in [key_from, key_to]
    ]
    words_along_possible_paths = [
        transfrom_path_into_word(path) + "A"
        for path in networkx.all_shortest_paths(
            keypadgraphs[keypadtype], *key_positions_from_and_to
        )
    ]
    return min(
        word_cost(KeypadType.DIRECTIONAL, word, layer + 1)
        for word in words_along_possible_paths
    )


print(sum(int(code[:-1]) * word_cost(KeypadType.NUMERIC, code, 0) for code in codes))
