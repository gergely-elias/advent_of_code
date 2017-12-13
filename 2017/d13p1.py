input_file = open('inputd13.txt','r')
input_lines = input_file.readlines()

import re

total_depth = int(re.findall('\d+', input_lines[-1])[0]) + 1
ranges = [0 for x in range(total_depth)]

for line in input_lines:
  line = line.strip()
  line = re.findall('\d+', line)
  ranges[int(line[0])] = int(line[1])

severity = 0
for depth in range(total_depth):
  if ranges[depth] > 0 and depth % (2 * ranges[depth] - 2) == 0:
    severity += ranges[depth] * depth

print severity
