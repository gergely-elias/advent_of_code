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

total_price = 0
for region in networkx.components.connected_components(garden_graph):
    region_graph = garden_graph.subgraph(region)
    area = len(region_graph.nodes)
    perimeter = 4 * len(region_graph.nodes) - 2 * len(region_graph.edges)
    total_price += area * perimeter
print(total_price)
