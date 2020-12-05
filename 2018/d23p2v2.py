input_file = open("inputd23.txt", "r")
input_lines = input_file.readlines()

import re
import math
import itertools

nanobots = [list(map(int, re.findall("-?\d+", line.strip()))) for line in input_lines]
dimension = len(nanobots[0]) - 1

range_extrema = [
    [
        min([nanobot[coord_index] - nanobot[dimension] for nanobot in nanobots]),
        max([nanobot[coord_index] + nanobot[dimension] for nanobot in nanobots]),
    ]
    for coord_index in range(dimension)
]
max_distance = max(
    range_extrema[coord_index][1] - range_extrema[coord_index][0]
    for coord_index in range(dimension)
)
start_size = 2 ** int(math.ceil(math.log(max_distance, 2)))


def smallest_coord_sum_in_cube(min_coords, cube_size):
    return sum(
        [
            min(abs(min_coords[coord_index]), abs(min_coords[coord_index] + cube_size))
            for coord_index in range(dimension)
            if min_coords[coord_index] * (min_coords[coord_index] + cube_size) > 0
        ]
    )


def is_in_range(point, bot, extra_distance):
    return (
        sum(
            [
                abs(point[coord_index] - bot[coord_index])
                for coord_index in range(dimension)
            ]
        )
        <= bot[dimension] + extra_distance
    )


def has_intersection(nanobot, min_coords, cube_size):
    corner_center_axis_distance = (cube_size - 1) * 0.5
    cube_center = [coord + corner_center_axis_distance for coord in min_coords]
    return is_in_range(cube_center, nanobot, dimension * corner_center_axis_distance)


def count_intersecting_ranges(min_coords, cube_size):
    return sum(
        [has_intersection(nanobot, min_coords, cube_size) for nanobot in nanobots]
    )


corner_coord = [range_extrema[coord_index][0] for coord_index in range(dimension)]
cubes = [
    tuple(
        corner_coord
        + [
            start_size,
            len(nanobots),
            smallest_coord_sum_in_cube(corner_coord, start_size),
        ]
    )
]
while len(cubes) > 0:
    cubes.sort(
        key=lambda cube: (-cube[dimension + 1], cube[dimension + 2], cube[dimension])
    )
    next_cube = cubes.pop(0)
    if next_cube[dimension] == 1:
        print(next_cube[dimension + 2])
        break
    else:
        subcube_size = next_cube[dimension] // 2
        for subcube in itertools.product(
            *[range(2) for coord_index in range(dimension)]
        ):
            corner_coord = [
                (big_cube_coord + axis_flag * subcube_size)
                for big_cube_coord, axis_flag in zip(next_cube[:dimension], subcube)
            ]
            cubes.append(
                tuple(
                    corner_coord
                    + [
                        subcube_size,
                        count_intersecting_ranges(corner_coord, subcube_size),
                        smallest_coord_sum_in_cube(corner_coord, subcube_size),
                    ]
                )
            )
