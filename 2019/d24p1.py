import fileinput
import copy
import collections
import itertools

input_lines = list(fileinput.input())

height = len(input_lines)
width = len(input_lines[0].strip())
grid = collections.defaultdict(lambda: ".")
for (row_index, col_index) in itertools.product(range(height), range(width)):
    grid[(row_index, col_index)] = input_lines[row_index][col_index]

previous_biodiversity_ratings = []
biodiversity_unique = True
while biodiversity_unique:
    next_grid = collections.defaultdict(lambda: ".")
    for current_cell in itertools.product(range(height), range(width)):
        neighbour_count = 0
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            neighbour = tuple(
                [cell + step for (cell, step) in zip(current_cell, direction)]
            )
            if grid[neighbour] == "#":
                neighbour_count += 1
        if grid[current_cell] == "#" and neighbour_count == 1:
            next_grid[current_cell] = "#"
        elif grid[current_cell] == "." and neighbour_count in [1, 2]:
            next_grid[current_cell] = "#"
    grid = copy.deepcopy(next_grid)

    cell_biodiversity_points = 1
    total_biodiversity_rating = 0
    for current_cell in itertools.product(range(height), range(width)):
        if grid[current_cell] == "#":
            total_biodiversity_rating += cell_biodiversity_points
        cell_biodiversity_points *= 2
    biodiversity_unique = total_biodiversity_rating not in previous_biodiversity_ratings
    previous_biodiversity_ratings.append(total_biodiversity_rating)
print(total_biodiversity_rating)
