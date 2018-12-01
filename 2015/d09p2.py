input_file = open('inputd09.txt','r')
input_lines = input_file.readlines()

distances = 8 * [0]
index = 0
for i in range(8):
  distances[i] = 8 * [0]

for i in range(8 - 1):
  for j in range(i + 1, 8):
    dist = int(input_lines[index].strip().split(' ')[-1])
    distances[i][j] = dist
    distances[j][i] = dist
    index += 1

import itertools
max_total_distance = 0
all_city_permutations = itertools.permutations(range(8))
for city_order in all_city_permutations:
  current_total_distance = 0
  for i in range(len(city_order) - 1):
    current_total_distance += distances[city_order[i]][city_order[i + 1]]
  if current_total_distance > max_total_distance:
    max_total_distance = current_total_distance
print max_total_distance
