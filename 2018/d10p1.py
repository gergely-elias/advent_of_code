import fileinput
import collections
import re

input_lines = list(fileinput.input())

points = [list(map(int, re.findall("-?\d+", line.strip()))) for line in input_lines]

time = 0
min_text_height = float("inf")
best_time = -1
while True:
    xmin = min([x_pos + x_vel * time for x_pos, y_pos, x_vel, y_vel in points])
    xmax = max([x_pos + x_vel * time for x_pos, y_pos, x_vel, y_vel in points])
    ymin = min([y_pos + y_vel * time for x_pos, y_pos, x_vel, y_vel in points])
    ymax = max([y_pos + y_vel * time for x_pos, y_pos, x_vel, y_vel in points])
    if ymax - ymin < min_text_height:
        min_text_height = ymax - ymin
        best_time = time
    else:
        break
    time += 1

lattice = collections.defaultdict(lambda: " ")
xmin = min([x_pos + x_vel * best_time for x_pos, y_pos, x_vel, y_vel in points])
xmax = max([x_pos + x_vel * best_time for x_pos, y_pos, x_vel, y_vel in points])
ymin = min([y_pos + y_vel * best_time for x_pos, y_pos, x_vel, y_vel in points])
ymax = max([y_pos + y_vel * best_time for x_pos, y_pos, x_vel, y_vel in points])
for x_pos, y_pos, x_vel, y_vel in points:
    x = x_pos + x_vel * best_time
    y = y_pos + y_vel * best_time
    lattice[x, y] = "#"

for y in range(ymin, ymax + 1):
    row = ""
    for x in range(xmin, xmax + 1):
        row += lattice[x, y]
    print(row)
