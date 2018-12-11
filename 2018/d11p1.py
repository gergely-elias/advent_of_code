input_file = open('inputd11.txt','r')
grid_id = int(input_file.readlines()[0])

grid_size = 300
square_size = 3

import collections
fuel_in_cell = collections.defaultdict(lambda: 0)
sum_from_top_left_to_cell = collections.defaultdict(lambda: 0)

max_value = -float("inf")
max_position = []

for x in range(1, grid_size + 1):
  rack_id = x + 10
  for y in range(1, grid_size + 1):
    fuel_in_cell[x,y] = ((y * rack_id + grid_id) * rack_id / 100) % 10 - 5
    sum_from_top_left_to_cell[x,y] = fuel_in_cell[x,y] + sum_from_top_left_to_cell[x - 1,y] + sum_from_top_left_to_cell[x,y - 1] - sum_from_top_left_to_cell[x - 1,y - 1]
    if x > square_size - 1 and y > square_size - 1:
      sum_in_square = sum_from_top_left_to_cell[x,y] - sum_from_top_left_to_cell[x - square_size,y] - sum_from_top_left_to_cell[x,y - square_size] + sum_from_top_left_to_cell[x - square_size,y - square_size]
      if sum_in_square > max_value:
        max_value = sum_in_square
        max_position = [x - square_size + 1, y - square_size + 1]

print ','.join(map(str,max_position))
