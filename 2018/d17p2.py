input_file = open("inputd17.txt", "r")
input_lines = input_file.readlines()

import sys
import re
import collections

sys.setrecursionlimit(5000)

water_map = collections.defaultdict(lambda: ".")

min_x = float("inf")
max_x = -float("inf")
min_y = float("inf")
max_y = -float("inf")
for line in input_lines:
    coord_x = list(
        map(int, re.findall("\d+", re.findall("x=([\d\.]+)", line.strip())[0]))
    )
    coord_y = list(
        map(int, re.findall("\d+", re.findall("y=([\d\.]+)", line.strip())[0]))
    )
    range_x = range(coord_x[0], coord_x[-1] + 1)
    range_y = range(coord_y[0], coord_y[-1] + 1)
    for x in range_x:
        for y in range_y:
            water_map[(y, x)] = "#"
    min_x = min(range_x[0], min_x)
    max_x = max(range_x[-1], max_x)
    min_y = min(range_y[0], min_y)
    max_y = max(range_y[-1], max_y)


def flow(source_y, source_x):
    if source_y > max_y:
        return
    if water_map[(source_y, source_x)] == ".":
        water_map[(source_y, source_x)] = "|"
    if water_map[(source_y + 1, source_x)] == ".":
        flow(source_y + 1, source_x)
    elif (
        water_map[(source_y + 1, source_x)] == "#"
        or water_map[(source_y + 1, source_x)] == "~"
    ):

        next_wall_right = None
        sink_or_wall_lookup = source_x + 1
        while (
            water_map[(source_y + 1, sink_or_wall_lookup)] == "#"
            or water_map[(source_y + 1, sink_or_wall_lookup)] == "~"
        ) and (
            water_map[(source_y, sink_or_wall_lookup)] == "."
            or water_map[(source_y, sink_or_wall_lookup)] == "|"
        ):
            if water_map[(source_y, sink_or_wall_lookup)] == ".":
                water_map[(source_y, sink_or_wall_lookup)] = "|"
            sink_or_wall_lookup += 1
        if water_map[(source_y + 1, sink_or_wall_lookup)] == ".":
            if water_map[(source_y, sink_or_wall_lookup)] == ".":
                water_map[(source_y, sink_or_wall_lookup)] = "|"
            flow(source_y + 1, sink_or_wall_lookup)
        elif water_map[(source_y, sink_or_wall_lookup)] == "#":
            next_wall_right = sink_or_wall_lookup

        next_wall_left = None
        sink_or_wall_lookup = source_x - 1
        while (
            water_map[(source_y + 1, sink_or_wall_lookup)] == "#"
            or water_map[(source_y + 1, sink_or_wall_lookup)] == "~"
        ) and (
            water_map[(source_y, sink_or_wall_lookup)] == "."
            or water_map[(source_y, sink_or_wall_lookup)] == "|"
        ):
            if water_map[(source_y, sink_or_wall_lookup)] == ".":
                water_map[(source_y, sink_or_wall_lookup)] = "|"
            sink_or_wall_lookup -= 1
        if water_map[(source_y + 1, sink_or_wall_lookup)] == ".":
            if water_map[(source_y, sink_or_wall_lookup)] == ".":
                water_map[(source_y, sink_or_wall_lookup)] = "|"
            flow(source_y + 1, sink_or_wall_lookup)
        elif water_map[(source_y, sink_or_wall_lookup)] == "#":
            next_wall_left = sink_or_wall_lookup

        if next_wall_left and next_wall_right:
            wall_to_wall_range_x = range(next_wall_left + 1, next_wall_right)
            for x in wall_to_wall_range_x:
                water_map[(source_y, x)] = "~"
            for x in wall_to_wall_range_x:
                if water_map[(source_y - 1, x)] == "|":
                    flow(source_y - 1, x)


water_spring_coords = (0, 500)
water_map[water_spring_coords] = "+"
flow(*water_spring_coords)

print(
    [v for (y, x), v in water_map.items() if (y in range(min_y, max_y + 1))].count("~")
)
