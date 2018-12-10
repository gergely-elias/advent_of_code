input_file = open('inputd10.txt','r')
input_lines = input_file.readlines()

import re

points = [map(int,re.findall('-?\d+', line.strip())) for line in input_lines]

time = 0
min_text_height = float("inf")
best_time = -1
while True:
  xmin = float("inf")
  xmax = -float("inf")
  ymin = float("inf")
  ymax = -float("inf")
  for point in points:
    x = point[0] + point[2] * time
    y = point[1] + point[3] * time
    xmin = min(x, xmin)
    xmax = max(x, xmax)
    ymin = min(y, ymin)
    ymax = max(y, ymax)
  if ymax - ymin < min_text_height:
    min_text_height = ymax - ymin
    best_time = time
  else:
    break
  time += 1

print best_time
