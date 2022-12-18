import fileinput
import itertools
import networkx

input_lines = list(fileinput.input())
dimensions = 3
mincoords = [float("inf")] * dimensions
maxcoords = [-float("inf")] * dimensions
lava_cubes = set()
for line in input_lines:
    lava_cube = tuple(map(int, line.strip().split(",")))
    lava_cubes.add(lava_cube)
    mincoords = [min(coords) for coords in zip(lava_cube, mincoords)]
    maxcoords = [max(coords) for coords in zip(lava_cube, maxcoords)]

side_directions = []
for coord_index in range(dimensions):
    for coord_direction in [1, -1]:
        direction = [0] * dimensions
        direction[coord_index] += coord_direction
        side_directions.append(tuple(direction))


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


air_graph = networkx.Graph()
for cube in itertools.product(
    *map(
        lambda x: list(range(x[0] - 1, x[1] + 2)),
        zip(mincoords, tuple_sum(maxcoords, [1] * dimensions)),
    )
):
    for coord_index in range(dimensions):
        if cube[coord_index] >= mincoords[coord_index]:
            neighbour_cell = list(cube)
            neighbour_cell[coord_index] -= 1
            neighbour_cell = tuple(neighbour_cell)
            if cube not in lava_cubes and neighbour_cell not in lava_cubes:
                air_graph.add_edge(cube, neighbour_cell)
external_air = networkx.node_connected_component(
    air_graph, tuple_sum(mincoords, [-1] * dimensions)
)

external_faces = 0
for lava_cube in lava_cubes:
    for direction in side_directions:
        if tuple_sum(lava_cube, direction) in external_air:
            external_faces += 1
print(external_faces)
