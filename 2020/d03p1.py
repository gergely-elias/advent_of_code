import fileinput

input_lines = list(fileinput.input())

grid = [line.strip() for line in input_lines]
height = len(grid)
width = len(grid[0])

x = 0
y = 0
number_of_trees = 0
while y < height:
    if grid[y][x % width] == "#":
        number_of_trees += 1
    y += 1
    x += 3
print(number_of_trees)
