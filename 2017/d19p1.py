input_file = open('inputd19.txt','r')
input_lines = input_file.readlines()

direction = 2
x = input_lines[0].index('|')
y = 0
letters_along_path = ''
neighbour_offsets = [(0, -1), (1, 0), (0, 1), (-1, 0)]

while y in range(len(input_lines)) and x in range(len(input_lines[y])) and input_lines[y][x] != ' ':
  if input_lines[y][x] not in ['|', '-', '+', ' ']:
    letters_along_path += input_lines[y][x]
  elif input_lines[y][x] == '+':
    lookaround_direction = (direction + 1) % 4
    lookaround_x = x + neighbour_offsets[lookaround_direction][0]
    lookaround_y = y + neighbour_offsets[lookaround_direction][1]
    if lookaround_y in range(len(input_lines)) and lookaround_x in range(len(input_lines[lookaround_y])) and input_lines[lookaround_y][lookaround_x] in ['|', '-']:
      direction = lookaround_direction
    else:
      direction = (lookaround_direction + 2) % 4
  x += neighbour_offsets[direction][0]
  y += neighbour_offsets[direction][1]

print letters_along_path
