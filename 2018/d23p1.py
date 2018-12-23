input_file = open('inputd23.txt','r')
input_lines = input_file.readlines()

import re

nanobots = []
for line in input_lines:
  nanobot = map(int, re.findall('-?\d+', line.strip()))
  nanobots.append(nanobot)
num_of_coords = len(nanobots[0]) - 1
radii = [nanobot[num_of_coords] for nanobot in nanobots]
nanobot_with_largest_radius = nanobots[radii.index(max(radii))]

def is_in_range(point, bot):
  dist = 0
  for coord in range(num_of_coords):
    dist += abs(point[coord] - bot[coord])
  return dist <= bot[num_of_coords]

bot_coords = [bot[:num_of_coords] for bot in nanobots]
print sum([is_in_range(bot_coord, nanobot_with_largest_radius) for bot_coord in bot_coords])
