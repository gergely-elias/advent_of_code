import fileinput
import itertools
import networkx

input_lines = list(fileinput.input())

garden = [row.strip() for row in input_lines]
height = len(garden)
width = len(garden[0])
source = (0, garden[0].index("."))
target = (height - 1, garden[-1].index("."))

garden_graph = networkx.Graph()
for y, row in enumerate(garden):
    for x, cell in enumerate(row):
        if cell != "#":
            if y > 0 and garden[y - 1][x] != "#":
                garden_graph.add_edge((y - 1, x), (y, x))
            if x > 0 and row[x - 1] != "#":
                garden_graph.add_edge((y, x - 1), (y, x))

junctions = [node for node in garden_graph.nodes() if garden_graph.degree[node] > 2]
crucial_nodes = junctions + [source, target]
simplified_garden_graph = networkx.Graph()
for node_pair in itertools.combinations(crucial_nodes, 2):
    reduced_garden_graph = garden_graph.subgraph(
        set(garden_graph.nodes).difference(crucial_nodes).union(node_pair)
    )
    if networkx.has_path(reduced_garden_graph, *node_pair):
        simplified_garden_graph.add_edge(
            *node_pair,
            weight=networkx.shortest_path_length(reduced_garden_graph, *node_pair)
        )

print(
    max(
        networkx.path_weight(simplified_garden_graph, path, "weight")
        for path in networkx.all_simple_paths(simplified_garden_graph, source, target)
    )
)
