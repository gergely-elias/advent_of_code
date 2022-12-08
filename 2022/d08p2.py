import fileinput
import math

input_lines = list(fileinput.input())
tree_grid = []

for line in input_lines:
    tree_grid.append(list(map(int, line.strip())))

maximal_scenic_score = 0
for y in range(len(tree_grid)):
    for x in range(len(tree_grid[0])):
        viewing_distances = []
        for direction_y, direction_x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            viewing_distance = 0
            lookup_y, lookup_x = y + direction_y, x + direction_x
            while lookup_y in range(len(tree_grid)) and lookup_x in range(
                len(tree_grid[0])
            ):
                viewing_distance += 1
                if tree_grid[lookup_y][lookup_x] < tree_grid[y][x]:
                    lookup_y, lookup_x = lookup_y + direction_y, lookup_x + direction_x
                else:
                    break
            viewing_distances.append(viewing_distance)
        scenic_score = math.prod(viewing_distances)
        if scenic_score > maximal_scenic_score:
            maximal_scenic_score = scenic_score
print(maximal_scenic_score)
