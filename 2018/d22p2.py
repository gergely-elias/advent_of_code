input_file = open('inputd22.txt','r')
input_lines = input_file.readlines()

import re
import networkx

cave_depth = int(re.findall('\d+', input_lines[0])[0])
target_x, target_y = map(int, re.findall('\d+', input_lines[1]))

cave_generator = [16807, 48271, 20183]
source_x, source_y = 0, 0
move_time = 1
equipment_switch_time = 7

geologic_index = dict()
erosion_level = dict()
region_type = dict()
distance = networkx.Graph()

beyond_target = 0
previous_beyond_target = -(target_y + 1)
for iteration in range(2):
  for y in range(target_y + beyond_target + 1):
    x_min = target_x + previous_beyond_target + 1 if y < target_y + previous_beyond_target else 0
    for x in range(x_min, target_x + beyond_target + 1):
      if (y, x) == (source_y, source_x) or (y, x) == (target_y, target_x):
        geologic_index[y, x] = 0
      elif y == 0:
        geologic_index[y, x] = x * cave_generator[0]
      elif x == 0:
        geologic_index[y, x] = y * cave_generator[1]
      else:
        geologic_index[y, x] = erosion_level[y, x - 1] * erosion_level[y - 1, x]
      erosion_level[y, x] = (geologic_index[y, x] + cave_depth) % cave_generator[2]
      region_type[y, x] = erosion_level[y, x] % 3

      current_region = [y, x]
      current_type = region_type[tuple(current_region)]
      possible_equipment = [(current_type + 1) % 3, (current_type + 2) % 3]
      distance.add_edge(tuple(current_region + [possible_equipment[0]]), tuple(current_region + [possible_equipment[1]]), weight = equipment_switch_time)
      for coord in range(len(current_region)):
        if current_region[coord] > 0:
          neighbour_region = current_region[:]
          neighbour_region[coord] -= 1
          neighbour_type = region_type[tuple(neighbour_region)]
          if current_type == neighbour_type:
            matching_equipment = possible_equipment
          else:
            matching_equipment = [3 - current_type - neighbour_type]
          for equipment in matching_equipment:
            distance.add_edge(tuple(current_region + [equipment]), tuple(neighbour_region + [equipment]), weight = move_time)

  shortest_path_length = networkx.dijkstra_path_length(distance, source = (source_y, source_x, 1), target = (target_y, target_x, 1), weight = 'weight')
  previous_beyond_target = beyond_target
  beyond_target = (shortest_path_length - target_x - target_y) // 2

print(shortest_path_length)
