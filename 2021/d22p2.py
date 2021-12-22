import fileinput
import re
import math

input_lines = list(fileinput.input())

input_cuboids = [
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
processed_cuboids = set()
axes = ["x", "y", "z"]

for cuboid in input_cuboids:
    switch, coords = cuboid
    next_processed_cuboids = processed_cuboids.copy()
    if switch:
        next_processed_cuboids.add((*[coords[axis] for axis in axes],))
    for prev_cuboid in processed_cuboids:
        if all(
            [
                coords[axis][0] > prev_cuboid[axis_index][1]
                or coords[axis][1] < prev_cuboid[axis_index][0]
                for axis_index, axis in enumerate(axes)
            ]
        ):
            pass
        else:
            next_processed_cuboids.remove(prev_cuboid)
            prev_axis_intersecting_regions = []
            for axis_index, axis in enumerate(axes):
                current_axis_regions = (
                    (
                        prev_cuboid[axis_index][0],
                        min(prev_cuboid[axis_index][1], coords[axis][0] - 1),
                    )
                    if coords[axis][0] > prev_cuboid[axis_index][0]
                    else None,
                    (
                        max(coords[axis][0], prev_cuboid[axis_index][0]),
                        min(coords[axis][1], prev_cuboid[axis_index][1]),
                    )
                    if coords[axis][0] <= prev_cuboid[axis_index][1]
                    and coords[axis][1] >= prev_cuboid[axis_index][0]
                    else None,
                    (
                        max(prev_cuboid[axis_index][0], coords[axis][1] + 1),
                        prev_cuboid[axis_index][1],
                    )
                    if prev_cuboid[axis_index][1] > coords[axis][1]
                    else None,
                )
                for region_index, region in enumerate(current_axis_regions):
                    if (
                        region_index != 1
                        and all(
                            prev_axis_intersection is not None
                            for prev_axis_intersection in prev_axis_intersecting_regions
                        )
                        and region is not None
                    ):
                        next_processed_cuboids.add(
                            (
                                *prev_axis_intersecting_regions,
                                region,
                                *prev_cuboid[axis_index + 1 :],
                            )
                        )
                prev_axis_intersecting_regions.append(current_axis_regions[1])
    processed_cuboids = next_processed_cuboids.copy()

print(
    sum(
        math.prod(max_coord - min_coord + 1 for min_coord, max_coord in cuboid)
        for cuboid in processed_cuboids
    )
)
