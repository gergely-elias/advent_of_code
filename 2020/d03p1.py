input_file = open('inputd03.txt','r')
input_lines = [line.strip() for line in input_file.readlines()]

height = len(input_lines)
width = len(input_lines[0])

x = 0
y = 0
number_of_trees = 0
while y < height:
  if input_lines[y][x % width] == '#':
    number_of_trees += 1
  y += 1
  x += 3
print(number_of_trees)
