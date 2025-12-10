import fileinput
import itertools

input_lines = list(fileinput.input())
corners = [tuple(map(int, line.strip().split(","))) for line in input_lines]

edges_horizontal = []
edges_vertical = []
for corner_index in range(len(corners)):
    corner_x, corner_y = corners[corner_index]
    next_corner_x, next_corner_y = corners[(corner_index + 1) % len(corners)]
    if corner_y == next_corner_y:
        edges_horizontal.append((corner_y, sorted([corner_x, next_corner_x])))
    if corner_x == next_corner_x:
        edges_vertical.append((corner_x, sorted([corner_y, next_corner_y])))

maximal_rectangle_area = 0
for (corner_a_x, corner_a_y), (corner_b_x, corner_b_y) in itertools.combinations(
    corners, 2
):
    rectangle_area = (abs(corner_a_x - corner_b_x) + 1) * (
        abs(corner_a_y - corner_b_y) + 1
    )
    if rectangle_area > maximal_rectangle_area:
        rectangle_x1, rectangle_x2 = sorted([corner_a_x, corner_b_x])
        rectangle_y1, rectangle_y2 = sorted([corner_a_y, corner_b_y])
        rectangle_is_inside = True
        if rectangle_is_inside:
            for edge_y, (edge_x1, edge_x2) in edges_horizontal:
                if (
                    rectangle_y1 < edge_y < rectangle_y2
                    and rectangle_x2 > edge_x1
                    and edge_x2 > rectangle_x1
                ):
                    rectangle_is_inside = False
                    break
        if rectangle_is_inside:
            for edge_x, (edge_y1, edge_y2) in edges_vertical:
                if (
                    rectangle_x1 < edge_x < rectangle_x2
                    and rectangle_y2 > edge_y1
                    and edge_y2 > rectangle_y1
                ):
                    rectangle_is_inside = False
                    break
        if rectangle_is_inside:
            maximal_rectangle_area = rectangle_area
print(maximal_rectangle_area)
