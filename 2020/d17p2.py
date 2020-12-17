import fileinput
import collections
import itertools

input_lines = list(fileinput.input())

dimensions = 4
neighbour_directions = set(itertools.product(range(-1, 2), repeat=dimensions))
neighbour_directions.remove(tuple([0] * dimensions))

grid = collections.defaultdict(lambda: 0)
mins = tuple([float("inf")] * dimensions)
maxs = tuple([-float("inf")] * dimensions)
active_cell_count = 0
for row_index, line in enumerate(input_lines):
    for column_index, cell in enumerate(line.strip()):
        if cell == "#":
            coord = tuple([column_index, row_index] + [0] * (dimensions - 2))
            grid[coord] = 1
            mins = tuple([min(c, m) for c, m in zip(coord, mins)])
            maxs = tuple([max(c, m) for c, m in zip(coord, maxs)])
            active_cell_count += 1

for step in range(6):
    previous_grid = grid.copy()
    active_cell_count = 0
    for coord in itertools.product(
        *[range(a - 1, b + 2) for (a, b) in zip(mins, maxs)]
    ):
        active_neighbours_count = sum(
            [
                previous_grid[
                    tuple([c + d for c, d in zip(coord, neighbour_direction)])
                ]
                for neighbour_direction in neighbour_directions
            ]
        )
        if (previous_grid[coord] == 1 and 2 <= active_neighbours_count <= 3) or (
            previous_grid[coord] == 0 and active_neighbours_count == 3
        ):
            grid[coord] = 1
            mins = tuple([min(c, m) for c, m in zip(coord, mins)])
            maxs = tuple([max(c, m) for c, m in zip(coord, maxs)])
        else:
            grid[coord] = 0
        active_cell_count += grid[coord]
print(active_cell_count)
