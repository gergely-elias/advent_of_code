import fileinput
import copy
import collections
import itertools

input_lines = list(fileinput.input())

height = len(input_lines)
width = len(input_lines[0].strip())
assert height % 2 == 1 and width % 2 == 1
center_coord = ((height - 1) // 2, (width - 1) // 2)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = collections.defaultdict(lambda: ".")
for (row_index, col_index) in itertools.product(range(height), range(width)):
    grid[(row_index, col_index)] = input_lines[row_index][col_index]

multilevel_grid = collections.defaultdict(lambda: collections.defaultdict(lambda: "."))
multilevel_grid[0] = grid

for iteration in range(200):
    next_multilevel_grid = collections.defaultdict(
        lambda: collections.defaultdict(lambda: ".")
    )
    for grid_level in range(-iteration - 1, iteration + 2):
        next_grid = collections.defaultdict(lambda: ".")
        for current in itertools.product(range(height), range(width)):
            if current == center_coord:
                continue
            neighbour_count = 0
            for direction in directions:
                zero_coord_index = direction.index(0)
                non_zero_coord_index = 1 - zero_coord_index
                size_in_direction = [height, width][non_zero_coord_index]
                size_in_normal_direction = [height, width][zero_coord_index]
                neighbour = tuple(
                    [cell + step for (cell, step) in zip(current, direction)]
                )
                if multilevel_grid[grid_level][neighbour] == "#":
                    neighbour_count += 1

                if neighbour[non_zero_coord_index] in [-1, size_in_direction]:
                    neighbour_count += (
                        1
                        if multilevel_grid[grid_level - 1][
                            tuple(
                                [
                                    cell + step
                                    for (cell, step) in zip(center_coord, direction)
                                ]
                            )
                        ]
                        == "#"
                        else 0
                    )

                if current == tuple(
                    [cell + step for (cell, step) in zip(center_coord, direction)]
                ):
                    neighbour_cell = [None] * 2
                    neighbour_cell[non_zero_coord_index] = (
                        size_in_direction - 1
                        if direction[non_zero_coord_index] == 1
                        else 0
                    )
                    for coord_loop in range(size_in_normal_direction):
                        neighbour_cell[zero_coord_index] = coord_loop
                        neighbour_count += (
                            1
                            if multilevel_grid[grid_level + 1][tuple(neighbour_cell)]
                            == "#"
                            else 0
                        )

            if multilevel_grid[grid_level][current] == "#" and neighbour_count == 1:
                next_grid[current] = "#"
            elif multilevel_grid[grid_level][current] == "." and neighbour_count in [
                1,
                2,
            ]:
                next_grid[current] = "#"
        next_multilevel_grid[grid_level] = next_grid
    multilevel_grid = copy.deepcopy(next_multilevel_grid)

bug_count = 0
for (level, line_index, col_index) in itertools.product(
    range(-iteration - 1, iteration + 2), range(height), range(width)
):
    if multilevel_grid[level][(line_index, col_index)] == "#":
        bug_count += 1
print(bug_count)
