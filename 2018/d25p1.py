input_file = open("inputd25.txt", "r")
input_lines = input_file.readlines()

import itertools
import re
import networkx


def dist(pair):
    return sum([abs(coord1 - coord2) for coord1, coord2 in zip(*pair)])


constellation = networkx.Graph()
points = []
for line in input_lines:
    point = tuple(map(int, re.findall("-?\d+", line.strip())))
    points.append(point)
    constellation.add_node(point)

for pair in itertools.combinations(points, 2):
    if dist(pair) <= 3:
        constellation.add_edge(*pair)

print(networkx.number_connected_components(constellation))
