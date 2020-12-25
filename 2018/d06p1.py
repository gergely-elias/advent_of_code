import fileinput
import collections
import re

input_lines = list(fileinput.input())

coordinates = [tuple(map(int, re.findall(r"\d+", line))) for line in input_lines]

minx = float("inf")
maxx = -float("inf")
miny = float("inf")
maxy = -float("inf")
for x, y in coordinates:
    minx = min(x, minx)
    maxx = max(x, maxx)
    miny = min(y, miny)
    maxy = max(y, maxy)

closest_coordinate = collections.defaultdict(lambda: "unknown")
coordinate_areas = collections.defaultdict(lambda: 0)
for location_y in range(miny, maxy + 1):
    for location_x in range(minx, maxx + 1):
        min_distance = float("inf")
        min_coord = "unknown"
        for cx, cy in coordinates:
            d = abs(cx - location_x) + abs(cy - location_y)
            if min_coord == "unknown" or d < min_distance:
                min_distance = d
                min_coord = (cx, cy)
            elif d == min_distance and min_coord != "tied":
                min_coord = "tied"
        closest_coordinate[(location_y, location_x)] = min_coord
        coordinate_areas[min_coord] += 1

coordinates_with_infinite_areas = set()
for location_y in range(miny, maxy + 1):
    coordinates_with_infinite_areas.add(closest_coordinate[(location_y, minx)])
    coordinates_with_infinite_areas.add(closest_coordinate[(location_y, maxx)])
for location_x in range(minx, maxx + 1):
    coordinates_with_infinite_areas.add(closest_coordinate[(miny, location_x)])
    coordinates_with_infinite_areas.add(closest_coordinate[(maxy, location_x)])

coordinates_with_finite_areas = {
    k: v
    for k, v in coordinate_areas.items()
    if k not in coordinates_with_infinite_areas and k != "tied"
}
print(max(coordinates_with_finite_areas.values()))
