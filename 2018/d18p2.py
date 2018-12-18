input_file = open('inputd18.txt','r')
input_lines = input_file.readlines()

import copy
import collections

landscape = collections.defaultdict(lambda: -1)
area_size = len(input_lines)

for y in range(area_size):
  line = input_lines[y].strip()
  for x in range(area_size):
    landscape[y, x] = ['.', '|', '#'].index(line[x])

target_minute = 1000000000
current_minute = 0
landscape_history = []
while True:
  next_landscape = copy.deepcopy(landscape)
  for y in range(area_size):
    for x in range(area_size):
      neighbourhood = [landscape[yn, xn] for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2)]
      if landscape[y, x] == 0 and neighbourhood.count(1) >= 3:
        next_landscape[y, x] = 1
      elif landscape[y, x] == 1 and neighbourhood.count(2) >= 3:
        next_landscape[y, x] = 2
      elif landscape[y, x] == 2 and (neighbourhood.count(2) < 2 or neighbourhood.count(1) < 1):
        next_landscape[y, x] = 0
  landscape = copy.deepcopy(next_landscape)
  if landscape in landscape_history:
    period = current_minute - landscape_history.index(landscape)
    matching_landscape = landscape_history[target_minute - 1 - (target_minute - 1 - landscape_history.index(landscape)) / period * period]
    print  matching_landscape.values().count(1) * matching_landscape.values().count(2)
    break
  else:
    landscape_history.append(copy.deepcopy(landscape))
  current_minute += 1
