input_file = open('inputd13.txt','r')
input_lines = input_file.readlines()

import re

ranges = {}

for line in input_lines:
  line = line.strip()
  line = re.findall('\d+', line)
  ranges[int(line[0])] = int(line[1])

severity = 0
for depth in ranges:
  if depth % (2 * ranges[depth] - 2) == 0:
    severity += ranges[depth] * depth

print severity
