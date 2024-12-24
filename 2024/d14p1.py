import collections
import fileinput
import math
import re

input_lines = list(fileinput.input())
robots = [list(map(int, re.findall(r"-?\d+", line.strip()))) for line in input_lines]
width = 101
height = 103
time = 100

center_x = (width - 1) // 2
center_y = (height - 1) // 2

quarters = collections.defaultdict(int)
for start_x, start_y, velocity_x, velocity_y in robots:
    final_x = (start_x + time * velocity_x) % width
    final_y = (start_y + time * velocity_y) % height
    if final_x != center_x and final_y != center_y:
        quarter_x = final_x > center_x
        quarter_y = final_y > center_y
        quarters[(quarter_x, quarter_y)] += 1

print(math.prod(quarters.values()))
