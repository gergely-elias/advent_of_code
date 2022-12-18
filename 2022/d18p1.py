import fileinput

input_lines = list(fileinput.input())

dimensions = 3
lava_cubes = set()
for line in input_lines:
    lava_cubes.add(tuple(map(int, line.strip().split(","))))


side_directions = []
for coord_index in range(dimensions):
    for coord_direction in [1, -1]:
        direction = [0] * dimensions
        direction[coord_index] += coord_direction
        side_directions.append(tuple(direction))


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


faces = 0
for lava_cube in lava_cubes:
    for direction in side_directions:
        if tuple_sum(lava_cube, direction) not in lava_cubes:
            faces += 1
print(faces)
