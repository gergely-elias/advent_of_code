import fileinput
import re

input_lines = list(fileinput.input())

claims = [list(map(int, re.findall("\d+", line.strip()))) for line in input_lines]

size_x = max([x + w for claim_id, x, y, w, h in claims])
size_y = max([y + h for claim_id, x, y, w, h in claims])

overlap_count = 0
fabric_map = [[0 for i in range(size_x)] for j in range(size_y)]
for claim in claims:
    claim_id, x, y, w, h = claim
    for i in range(x, x + w):
        for j in range(y, y + h):
            if fabric_map[j][i] == 0:
                fabric_map[j][i] = claim_id
            elif fabric_map[j][i] != -1:
                fabric_map[j][i] = -1
                overlap_count += 1

print(overlap_count)
