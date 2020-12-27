import fileinput
import re

input_lines = list(fileinput.input())

valid_triangles = 0
all_sides = []

for line in input_lines:
    sides = [int(x) for x in re.findall(r"\d+", line.strip())]
    all_sides.extend(sides)

for i in range(0, len(all_sides), 9):
    triplet = all_sides[i : i + 9]
    for j in range(3):
        sides = triplet[j::3]
        if max(sides) * 2 < sum(sides):
            valid_triangles += 1
print(valid_triangles)
