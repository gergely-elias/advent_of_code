import fileinput
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


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

total_price = 0
for region in networkx.components.connected_components(garden_graph):
    region_graph = garden_graph.subgraph(region)
    area = len(region_graph.nodes)

    sides = 0
    for border_direction, orthogonal_direction in zip(
        DIRECTIONS, DIRECTIONS[1:] + DIRECTIONS[:1]
    ):
        borders_in_direction = [
            plot
            for plot in region_graph.nodes
            if tuple_sum(plot, border_direction) not in region_graph.nodes
        ]
        first_borders_on_side = [
            border
            for border in borders_in_direction
            if tuple_sum(border, orthogonal_direction) not in borders_in_direction
        ]
        sides += len(first_borders_on_side)
    total_price += area * sides
print(total_price)
