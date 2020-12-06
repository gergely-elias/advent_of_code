import fileinput

input_lines = list(fileinput.input())

grid = [line.strip() for line in input_lines]
height = len(grid)
width = len(grid[0])

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
product = 1
for slope in slopes:
    x = 0
    y = 0
    number_of_trees = 0
    while y < height:
        if grid[y][x % width] == "#":
            number_of_trees += 1
        y += slope[0]
        x += slope[1]
    product *= number_of_trees
print(product)
