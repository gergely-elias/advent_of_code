import fileinput
import math

input_lines = list(fileinput.input())

height = len(input_lines)
width = len(input_lines[0].strip())
asteroidmap = []
for line_index in range(len(input_lines)):
    asteroidmap.append(input_lines[line_index].strip())

maxcount = 0
for candidate_y in range(height):
    for candidate_x in range(width):
        count = 0
        if asteroidmap[candidate_y][candidate_x] == "#":
            for other_y in range(height):
                for other_x in range(width):
                    if asteroidmap[other_y][other_x] == "#" and (
                        other_y != candidate_y or other_x != candidate_x
                    ):
                        distance_y = other_y - candidate_y
                        distance_x = other_x - candidate_x
                        divisor = math.gcd(abs(distance_y), abs(distance_x))
                        distance_y_unit = distance_y // divisor
                        distance_x_unit = distance_x // divisor
                        visible = True
                        for step in range(1, divisor):
                            if (
                                asteroidmap[candidate_y + step * distance_y_unit][
                                    candidate_x + step * distance_x_unit
                                ]
                                == "#"
                            ):
                                visible = False
                                break
                        if visible:
                            count += 1
        if count > maxcount:
            maxcount = count
print(maxcount)
