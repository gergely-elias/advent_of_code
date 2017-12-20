input_file = open('inputd20.txt','r')
input_lines = input_file.readlines()

import re
import operator

particles = []

for line in input_lines:
  line = line.strip()
  line = re.findall('<[^>]*>', line)
  particle = {}
  particle['position'] = map(int, re.findall('-?\d+', line[0]))
  particle['velocity'] = map(int, re.findall('-?\d+', line[1]))
  particle['acceleration'] = map(int, re.findall('-?\d+', line[2]))
  particles.append(particle)

for particle in particles:
  for coordinate_index in range(3):
    if particle['acceleration'][coordinate_index] < 0:
      particle['acceleration'][coordinate_index] = - particle['acceleration'][coordinate_index]
      particle['velocity'][coordinate_index] = - particle['velocity'][coordinate_index]
      particle['position'][coordinate_index] = - particle['position'][coordinate_index]
    elif particle['acceleration'][coordinate_index] == 0 and particle['velocity'][coordinate_index] < 0:
      particle['velocity'][coordinate_index] = - particle['velocity'][coordinate_index]
      particle['position'][coordinate_index] = - particle['position'][coordinate_index]
    elif particle['acceleration'][coordinate_index] == 0 and particle['velocity'][coordinate_index] == 0 and particle['position'][coordinate_index] < 0:
      particle['position'][coordinate_index] = - particle['position'][coordinate_index]

  particle['acceleration_size'] = sum(particle['acceleration'])
  particle['velocity_size'] = sum(particle['velocity'])
  particle['position_size'] = sum(particle['position'])

closest_particle = sorted(particles, key=operator.itemgetter('acceleration_size', 'velocity_size', 'position_size'))[0]
print particles.index(closest_particle)
