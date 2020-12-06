import fileinput
import math

input_lines = list(fileinput.input())

height = len(input_lines)
width = len(input_lines[0].strip())
asteroidmap = []
for line_index in range(len(input_lines)):
    asteroidmap.append(input_lines[line_index].strip())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


maxcount = 0
maxcoord = None
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
                        divisor = gcd(abs(distance_y), abs(distance_x))
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
            maxcoord = [candidate_y, candidate_x]

laser_y, laser_x = maxcoord
targets = []
for target_y in range(height):
    for target_x in range(width):
        if asteroidmap[target_y][target_x] == "#" and (
            target_y != laser_y or target_x != laser_x
        ):
            targets.append(
                {
                    "direction": -math.atan2(target_x - laser_x, target_y - laser_y),
                    "distance": (target_y - laser_y) ** 2 + (target_x - laser_x) ** 2,
                    "x": target_x,
                    "y": target_y,
                }
            )
targets.sort(key=lambda target: (target["direction"], target["distance"]))

sort_index = 0
while sort_index != len(targets) - 2:
    if (
        len(
            set(
                [
                    targets[unsorted_target_index]["direction"]
                    for unsorted_target_index in range(sort_index, len(targets))
                ]
            )
        )
        == 1
    ):
        break
    if targets[sort_index]["direction"] == targets[sort_index + 1]["direction"]:
        targets.append(targets.pop(sort_index + 1))
    else:
        sort_index += 1

target = targets[199]
print(target["x"] * 100 + target["y"])
