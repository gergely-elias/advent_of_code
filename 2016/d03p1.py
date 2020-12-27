import fileinput
import re

input_lines = list(fileinput.input())

valid_triangles = 0

for line in input_lines:
    sides = [int(x) for x in re.findall(r"\d+", line.strip())]
    if max(sides) * 2 < sum(sides):
        valid_triangles += 1
print(valid_triangles)
