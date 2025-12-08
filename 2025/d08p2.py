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

pairs_in_proximity_order = [
    pair
    for (_, pair) in sorted(
        [(distance, boxes) for boxes, distance in box_distance_squares.items()]
    )
]

box_network = networkx.Graph()
for box_position in junction_box_positions:
    box_network.add_node(box_position)
for close_pair in pairs_in_proximity_order:
    box_network.add_edge(*close_pair)
    if networkx.is_connected(box_network):
        print(math.prod(box[0] for box in close_pair))
        break
