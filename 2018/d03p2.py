import fileinput
import collections
import re

input_lines = list(fileinput.input())

claims = [list(map(int, re.findall(r"\d+", line.strip()))) for line in input_lines]

size_x = max([x + w for claim_id, x, y, w, h in claims])
size_y = max([y + h for claim_id, x, y, w, h in claims])

fabric_map = [[0 for i in range(size_x)] for j in range(size_y)]
for claim in claims:
    claim_id, x, y, w, h = claim
    for i in range(x, x + w):
        for j in range(y, y + h):
            if fabric_map[j][i] == 0:
                fabric_map[j][i] = claim_id
            else:
                fabric_map[j][i] = -1

claim_areas = collections.defaultdict(lambda: 0)
for i in range(size_x):
    for j in range(size_y):
        claim_areas[fabric_map[j][i]] += 1

for claim in claims:
    [claim_id, x, y, w, h] = claim
    if claim_areas[claim_id] == w * h:
        print(claim_id)
        break
