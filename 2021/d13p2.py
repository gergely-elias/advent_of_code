import fileinput
import re

input_lines = list(fileinput.input())
separator_line_index = input_lines.index("\n")

dots = set(
    tuple(map(int, line.strip().split(",")))
    for line in input_lines[:separator_line_index]
)

folds = [
    [(axis, int(value)) for axis, value in re.findall(r"(\w)=(\d+)", line)][0]
    for line in input_lines[separator_line_index + 1 :]
]


def fold_point_along_axis(axis_index, axis_value, point):
    return tuple(
        2 * axis_value - coord if coord_index == axis_index else coord
        for coord_index, coord in enumerate(point)
    )


for fold in folds:
    axis_name, axis_value = fold
    next_dots = dots.copy()
    axis_index = "xy".index(axis_name)
    for dot in dots:
        if dot[axis_index] > axis_value:
            next_dots.add(fold_point_along_axis(axis_index, axis_value, dot))
            next_dots.remove(dot)
        elif dot[axis_index] == axis_value:
            next_dots.remove(dot)
    dots = next_dots.copy()

for y in range(min(dot[1] for dot in dots), max(dot[1] for dot in dots) + 1):
    for x in range(min(dot[0] for dot in dots), max(dot[0] for dot in dots) + 1):
        print("X" if (x, y) in dots else " ", end="")
    print("")
