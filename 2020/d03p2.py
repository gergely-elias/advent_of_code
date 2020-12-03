input_file = open('inputd03.txt','r')
input_lines = [line.strip() for line in input_file.readlines()]

height = len(input_lines)
width = len(input_lines[0])

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
product = 1
for slope in slopes:
  x = 0
  y = 0
  number_of_trees = 0
  while y < height:
    if input_lines[y][x % width] == '#':
      number_of_trees += 1
    y += slope[0]
    x += slope[1]
  product *= number_of_trees
print(product)
