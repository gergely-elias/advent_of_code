input_file = open('inputd22.txt','r')
input_lines = input_file.readlines()

import collections

init_grid_radius = (len(input_lines) - 1) / 2
grid_state = collections.defaultdict(lambda: 0)

for iy,line in enumerate(input_lines):
  line = line.strip()
  for ix in range(2 * init_grid_radius + 1):
    grid_state[(iy - init_grid_radius, ix - init_grid_radius)] = 1 if line[ix] == '#' else 0

x = 0
y = 0
direction = 0
neighbour_offsets = [(0, -1), (1, 0), (0, 1), (-1, 0)]
turn_amount_on_state = [-1, 1]
infection_count = 0
for step in range(10000):
  direction = (direction + turn_amount_on_state[grid_state[(y, x)]]) % 4
  grid_state[(y, x)] = (grid_state[(y, x)] + 1) % 2
  if grid_state[(y, x)] == 1:
    infection_count += 1
  x, y = map(sum, zip((x, y), neighbour_offsets[direction]))
print infection_count
