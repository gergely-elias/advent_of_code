input_file = open('inputd13.txt','r')
input_lines = input_file.readlines()

import re

ranges = {}

for line in input_lines:
  line = line.strip()
  line = re.findall('\d+', line)
  ranges[int(line[0])] = int(line[1])

delay = -1
caught = True

while caught:
  delay += 1
  caught = False
  for depth in ranges:
    if (depth + delay) % (2 * ranges[depth] - 2) == 0:
      caught = True
      break

print(delay)
