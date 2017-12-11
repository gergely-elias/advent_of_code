input_file = open('inputd11.txt','r')
input_lines = input_file.readlines()

line = input_lines[0].strip().split(',')
cube_coordinate = [0, 0, 0]
maximal_distance = 0
for direction in line:
  if direction == 's':
    cube_coordinate[2] += 1
    cube_coordinate[1] += -1
  elif direction == 'n':
    cube_coordinate[2] += -1
    cube_coordinate[1] += 1
  elif direction == 'ne':
    cube_coordinate[0] += 1
    cube_coordinate[2] += -1
  elif direction == 'sw':
    cube_coordinate[0] += -1
    cube_coordinate[2] += 1
  elif direction == 'nw':
    cube_coordinate[2] += 1
    cube_coordinate[0] += -1
  elif direction == 'se':
    cube_coordinate[2] += -1
    cube_coordinate[0] += 1
  maximal_distance = max(maximal_distance, max([abs(coordinate) for coordinate in cube_coordinate]))
print maximal_distance


