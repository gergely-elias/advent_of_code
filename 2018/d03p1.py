input_file = open('inputd03.txt','r')
input_lines = input_file.readlines()

import re

claims = [map(int, re.findall('\d+', line.strip())) for line in input_lines]

size_x = 0
size_y = 0
for claim in claims:
  [claim_id, x, y, w, h] = claim
  size_x = max(size_x, x + w)
  size_y = max(size_y, y + h)

overlap_count = 0
fabric_map = [[0 for i in range(size_x)] for j in range(size_y)]
for claim in claims:
  [claim_id, x, y, w, h] = claim
  for i in range(x, x + w):
    for j in range(y, y + h):
      if fabric_map[j][i] == 0:
        fabric_map[j][i] = claim_id
      elif fabric_map[j][i] != -1:
        fabric_map[j][i] = -1
        overlap_count += 1

print overlap_count
