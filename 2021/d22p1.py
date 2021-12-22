import fileinput
import re
import collections
import itertools

input_lines = list(fileinput.input())
cuboids = [
    (
        line.strip().startswith("on"),
        {
            axis: (int(min_value), int(max_value))
            for axis, min_value, max_value in re.findall(
                r"(\w)\=(-?\d+)\.\.(-?\d+)", line.strip()
            )
        },
    )
    for line in input_lines
]

axes = ["x", "y", "z"]
cubes_on = collections.defaultdict(lambda: False)
initialization_region_limits = (-50, 50)
for cuboid in cuboids:
    switch, coords = cuboid
    for cube_coords in itertools.product(
        *[
            range(
                max(initialization_region_limits[0], coords[axis][0]),
                min(initialization_region_limits[1], coords[axis][1]) + 1,
            )
            for axis in axes
        ]
    ):
        cubes_on[cube_coords] = switch
print(sum(cubes_on.values()))
