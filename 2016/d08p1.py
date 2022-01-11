import fileinput
import re

input_lines = list(fileinput.input())

width = 50
height = 6

pixels = [[0 for x in range(width)] for y in range(6)]
for line in input_lines:
    command = line.strip()
    if line[:4] == "rect":
        rect_size = list(map(int, re.findall(r"\d+", command)))
        for x in range(rect_size[0]):
            for y in range(rect_size[1]):
                pixels[y][x] = 1
    else:
        rot_size = list(map(int, re.findall(r"\d+", command)))
        if line[7] == "c":
            values = [pixels[y][rot_size[0]] for y in range(height)]
            for y in range(height):
                pixels[(y + rot_size[1]) % height][rot_size[0]] = values[y]
        else:
            values = [pixels[rot_size[0]][x] for x in range(width)]
            for x in range(width):
                pixels[rot_size[0]][(x + rot_size[1]) % width] = values[x]
        map(int, re.findall(r"\d+", command))
print(sum(sum(i) for i in pixels))
