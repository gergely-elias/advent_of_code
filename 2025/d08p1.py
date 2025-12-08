import collections
import fileinput
import itertools
import math
import networkx

input_lines = list(fileinput.input())
junction_box_positions = [
    tuple(map(int, line.strip().split(","))) for line in input_lines
]
box_distance_squares = collections.defaultdict(int)
for position_pair in itertools.combinations(junction_box_positions, 2):
    box_distance_squares[position_pair] = sum(
        (coord_a - coord_b) ** 2 for coord_a, coord_b in zip(*position_pair)
    )

CLOSEST_PAIRS_COUNT = 1000
closest_pairs = [
    pair
    for (_, pair) in sorted(
        [(distance, boxes) for boxes, distance in box_distance_squares.items()]
    )[:CLOSEST_PAIRS_COUNT]
]

box_network = networkx.Graph()
for box_position in junction_box_positions:
    box_network.add_node(box_position)
for close_pair in closest_pairs:
    box_network.add_edge(*close_pair)

LARGEST_CIRCUITS_COUNT = 3
print(
    math.prod(
        sorted(
            [len(component) for component in networkx.connected_components(box_network)]
        )[-LARGEST_CIRCUITS_COUNT:]
    )
)
