input_file = open('inputd11.txt','r')
input_lines = input_file.readlines()

line = input_lines[0].strip().split(',')
cube_coordinate = [0, 0, 0]
possible_directions = ['ne', 'sw', 'nw', 'se', 's', 'n']
for direction in line:
  direction_index = possible_directions.index(direction)
  cube_coordinate[direction_index / 2] += -1 if direction_index % 2 else 1
  cube_coordinate[(direction_index / 2 + 2) % 3] += 1 if direction_index % 2 else -1
print max([abs(coordinate) for coordinate in cube_coordinate])
