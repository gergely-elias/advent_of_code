import fileinput
import networkx
import math

input_lines = list(fileinput.input())
heights = [list(map(int, list(line.strip()))) for line in input_lines]

locations = networkx.Graph()
for y in range(len(heights)):
    for x in range(len(heights[0])):
        if x > 0 and heights[y][x] < 9 and heights[y][x - 1] < 9:
            locations.add_edge((y, x), (y, x - 1))
        if y > 0 and heights[y][x] < 9 and heights[y - 1][x] < 9:
            locations.add_edge((y, x), (y - 1, x))

print(
    math.prod(
        sorted(
            [len(basin) for basin in list(networkx.connected_components(locations))]
        )[-3:]
    )
)
