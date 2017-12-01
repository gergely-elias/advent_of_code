input_file = open('inputd03.txt','r')
input_lines = input_file.readlines()

start_x = 0
start_y = 0
start_position = (start_x, start_y)
houses_visited = set()
houses_visited.add(start_position)
current_positions = []

number_of_santas = 2
for santa_index in range(number_of_santas):
  current_positions.append(start_position)

santa_index = 0
for character in input_lines[0]:
  santa_index = (santa_index + 1) % number_of_santas
  (current_x, current_y) = current_positions[santa_index]
  if character == '^':
    current_y += 1
  elif character == 'v':
    current_y -= 1
  elif character == '>':
    current_x += 1
  elif character == '<':
    current_x -= 1
  current_positions[santa_index] = (current_x, current_y)
  houses_visited.add(current_positions[santa_index]) 

print len(houses_visited)

