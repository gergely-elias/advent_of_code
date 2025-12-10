import fileinput
import itertools

input_lines = list(fileinput.input())
corners = [tuple(map(int, line.strip().split(","))) for line in input_lines]

maximal_rectangle_area = 0
for (corner_a_x, corner_a_y), (corner_b_x, corner_b_y) in itertools.combinations(
    corners, 2
):
    rectangle_area = (abs(corner_a_x - corner_b_x) + 1) * (
        abs(corner_a_y - corner_b_y) + 1
    )
    maximal_rectangle_area = max(maximal_rectangle_area, rectangle_area)
print(maximal_rectangle_area)
