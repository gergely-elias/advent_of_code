import fileinput
import collections

cavemap = collections.defaultdict(lambda: ".")
input_lines = list(fileinput.input())
y_max = -float("inf")
for line in input_lines:
    points = line.strip().split(" -> ")
    x_prev, y_prev = None, None
    for idx, point in enumerate(points):
        x_coord, y_coord = map(int, point.split(","))
        y_max = max(y_max, y_coord)
        if idx > 0:
            if x_prev == x_coord:
                for y in range(min(y_prev, y_coord), max(y_prev, y_coord) + 1):
                    cavemap[(x_coord, y)] = "#"
            elif y_prev == y_coord:
                for x in range(min(x_prev, x_coord), max(x_prev, x_coord) + 1):
                    cavemap[(x, y_coord)] = "#"
            else:
                raise ValueError
        x_prev, y_prev = x_coord, y_coord

source = (500, 0)


def next_coord(x, y):
    if cavemap[(x, y + 1)] == ".":
        y += 1
    elif cavemap[(x - 1, y + 1)] == ".":
        y += 1
        x -= 1
    elif cavemap[(x + 1, y + 1)] == ".":
        y += 1
        x += 1
    return x, y


sand_at_rest = 0
y_sand = 1
while y_sand > 0:
    y_prev = -1
    x_sand, y_sand = source
    while y_sand > y_prev and y_sand <= y_max:
        y_prev = y_sand
        x_sand, y_sand = next_coord(x_sand, y_sand)
    cavemap[(x_sand, y_sand)] = "o"
    sand_at_rest += 1
print(sand_at_rest)
