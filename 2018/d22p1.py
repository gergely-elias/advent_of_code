input_file = open('inputd22.txt','r')
input_lines = input_file.readlines()

import re

cave_depth = int(re.findall('\d+', input_lines[0])[0])
target_x, target_y = map(int, re.findall('\d+', input_lines[1]))

cave_generator = [16807, 48271, 20183]
source_x, source_y = 0, 0

geologic_index = dict()
erosion_level = dict()
region_type = dict()

risk_level = 0
for y in range(target_y + 1):
  for x in range(target_x + 1):
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
    risk_level += region_type[y, x]

print(risk_level)
