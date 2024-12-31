import fileinput
import itertools
import networkx

input_lines = list(fileinput.input())
garden = [line.strip() for line in input_lines]
height = len(garden)
width = len(garden[0])

garden_graph = networkx.Graph()
for y in range(height):
    for x in range(width):
        garden_graph.add_node((y, x))
        if y > 0:
            if garden[y][x] == garden[y - 1][x]:
                garden_graph.add_edge((y, x), (y - 1, x))
        if x > 0:
            if garden[y][x] == garden[y][x - 1]:
                garden_graph.add_edge((y, x), (y, x - 1))


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


DIAGONAL_AND_NEIGHBOUR_DIRECTIONS = {
    diagonal_direction: [(diagonal_direction[0], 0), (0, diagonal_direction[1])]
    for diagonal_direction in itertools.product([-1, 1], repeat=2)
}

total_price = 0
for region in networkx.components.connected_components(garden_graph):
    region_graph = garden_graph.subgraph(region)
    area = len(region_graph.nodes)

    corner_count = 0
    for plot in region_graph.nodes:
        for (
            diagonal_direction,
            neighbour_directions,
        ) in DIAGONAL_AND_NEIGHBOUR_DIRECTIONS.items():
            neighbours = [
                tuple_sum(neighbour_direction, plot)
                for neighbour_direction in neighbour_directions
            ]
            neighbours_in_region = [
                neighbour in region_graph.nodes for neighbour in neighbours
            ]
            if not any(neighbours_in_region):
                corner_count += 1
            elif all(neighbours_in_region):
                diagonal = tuple_sum(diagonal_direction, plot)
                diagonal_in_region = diagonal in region_graph.nodes
                if not diagonal_in_region:
                    corner_count += 1
    total_price += area * corner_count
print(total_price)
