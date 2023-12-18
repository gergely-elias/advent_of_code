import fileinput

input_lines = list(fileinput.input())
instructions = [
    (dire, int(dist))
    for dire, dist in [line.strip().split()[:2] for line in input_lines]
]
direction_coordinates = {"D": (1, 0), "R": (0, 1), "U": (-1, 0), "L": (0, -1)}


def tuple_sum(*t):
    return tuple(sum(coords) for coords in zip(*t))


def tuple_scalar(t, s):
    return tuple(c * s for c in t)


current_coords = (0, 0)
vertices = [current_coords]
perimeter = 0
for direction, distance in instructions:
    current_coords = tuple_sum(
        current_coords, tuple_scalar(direction_coordinates[direction], distance)
    )
    vertices.append(current_coords)
    perimeter += distance

signed_double_area = 0
for (y1, x1), (y2, x2) in zip(vertices[:-1], vertices[1:]):
    signed_double_area += y1 * x2 - y2 * x1
print(abs(signed_double_area // 2) + perimeter // 2 + 1)
