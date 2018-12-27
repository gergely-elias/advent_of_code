input_file = open('inputd23.txt','r')
input_lines = input_file.readlines()

import re
import math
import itertools

nanobots = []
for line in input_lines:
  nanobot = map(int, re.findall('-?\d+', line.strip()))
  nanobots.append(nanobot)
num_of_coords = len(nanobots[0]) - 1

range_extrema = [[float("inf"), -float("inf")] for coord_index in range(num_of_coords)]
for nanobot in nanobots:
  for coord_index in range(num_of_coords):
    range_extrema[coord_index][0] = min(range_extrema[coord_index][0], nanobot[coord_index] - nanobot[num_of_coords])
    range_extrema[coord_index][1] = max(range_extrema[coord_index][1], nanobot[coord_index] + nanobot[num_of_coords])
max_distance = max(range_extrema[coord_index][1] - range_extrema[coord_index][0] for coord_index in range(num_of_coords))
start_size = 2 ** int(math.ceil(math.log(max_distance, 2)))

def smallest_coord_sum_in_cube(min_coords, cube_size):
  smallest_coord_sum = 0
  for coord_index in range(num_of_coords):
    if min_coords[coord_index] * (min_coords[coord_index] + cube_size) > 0:
      smallest_coord_sum += min(min_coords[coord_index], min_coords[coord_index] + cube_size)
  return smallest_coord_sum

def is_in_range(point, bot, extra_distance):
  dist = 0
  for coord in range(num_of_coords):
    dist += abs(point[coord] - bot[coord])
  return dist <= bot[num_of_coords] + extra_distance

def has_intersection(nanobot, min_coords, cube_size):
  corner_center_axis_distance = (cube_size - 1) * 0.5
  cube_center = [coord + corner_center_axis_distance for coord in min_coords]
  return is_in_range(cube_center, nanobot, num_of_coords * corner_center_axis_distance)

def count_intersecting_ranges(min_coords, cube_size):
  count = 0
  for nanobot in nanobots:
    if has_intersection(nanobot, min_coords, cube_size):
      count += 1
  return count

cubes = [tuple([range_extrema[coord_index][0] for coord_index in range(num_of_coords)] + [start_size, len(nanobots), smallest_coord_sum_in_cube([range_extrema[coord_index][0] for coord_index in range(num_of_coords)], start_size)])]
while len(cubes) > 0:
  cubes.sort(key = lambda job: (-job[num_of_coords + 1], job[num_of_coords + 2]))
  next_cube = cubes.pop(0)
  if next_cube[num_of_coords] == 1:
    print next_cube[num_of_coords + 2]
    break
  else:
    subcube_size = next_cube[num_of_coords] / 2
    for subcube in itertools.product(*[range(2) for coord_index in range(num_of_coords)]):
      corner_coord = [(corner_coord + axis_flag * subcube_size) for corner_coord, axis_flag in zip(next_cube[:num_of_coords], subcube)]
      cubes.append(tuple(corner_coord + [subcube_size, count_intersecting_ranges(corner_coord, subcube_size), smallest_coord_sum_in_cube(corner_coord, subcube_size)]))
smallest_coord_sum_in_cube
