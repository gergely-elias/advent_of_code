import fileinput

input_lines = list(fileinput.input())
tree_grid = []

for line in input_lines:
    tree_grid.append(list(map(int, line.strip())))

visible_trees = 0
for y in range(len(tree_grid)):
    for x in range(len(tree_grid[0])):
        if (
            all(tree_grid[lookup_y][x] < tree_grid[y][x] for lookup_y in range(0, y))
            or all(
                tree_grid[lookup_y][x] < tree_grid[y][x]
                for lookup_y in range(y + 1, len(tree_grid))
            )
            or all(tree_grid[y][lookup_x] < tree_grid[y][x] for lookup_x in range(0, x))
            or all(
                tree_grid[y][lookup_x] < tree_grid[y][x]
                for lookup_x in range(x + 1, len(tree_grid[0]))
            )
        ):
            visible_trees += 1
print(visible_trees)
