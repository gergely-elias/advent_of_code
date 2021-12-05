import fileinput
import re
import collections

input_lines = list(fileinput.input())

point_covers = collections.defaultdict(lambda: 0)
for line in input_lines:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
    if x1 == x2:
        for coord_loop in range(min(y1, y2), max(y1, y2) + 1):
            point_covers[x1, coord_loop] += 1
    elif y1 == y2:
        for coord_loop in range(min(x1, x2), max(x1, x2) + 1):
            point_covers[coord_loop, y1] += 1
    elif y2 - y1 == x2 - x1:
        for coord_loop in range(min(x1, x2), max(x1, x2) + 1):
            point_covers[coord_loop, y1 - x1 + coord_loop] += 1
    elif y1 - y2 == x2 - x1:
        for coord_loop in range(min(x1, x2), max(x1, x2) + 1):
            point_covers[coord_loop, y1 + x1 - coord_loop] += 1

print(sum([1 for cell_value in point_covers.values() if cell_value > 1]))
