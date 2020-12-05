input_file = open("inputd10.txt", "r")
input_lines = input_file.readlines()

import re

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

print(best_time)
