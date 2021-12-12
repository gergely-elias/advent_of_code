import fileinput
import networkx
import itertools
import math

input_lines = list(fileinput.input())

cave_connections = networkx.Graph()
for connected_cave_pair in [line.strip().split("-") for line in input_lines]:
    cave_connections.add_edge(*connected_cave_pair)

big_caves = [x for x in cave_connections.nodes() if x.isupper()]
small_caves = [x for x in cave_connections.nodes() if x not in big_caves]

small_cave_reduced_connections = networkx.Graph()
for small_cave_pair in itertools.combinations(small_caves, 2):
    small_cave_reduced_connections.add_edge(
        *small_cave_pair,
        weight=sum(
            all(cave not in small_caves for cave in cave_path[1:-1])
            for cave_path in networkx.all_simple_paths(
                cave_connections, source=small_cave_pair[0], target=small_cave_pair[1]
            )
        )
    )

total_paths = 0
for small_cave_edge_path in networkx.all_simple_edge_paths(
    small_cave_reduced_connections, source="start", target="end"
):
    total_paths += math.prod(
        [
            small_cave_reduced_connections.get_edge_data(*small_cave_reduced_edge)[
                "weight"
            ]
            for small_cave_reduced_edge in small_cave_edge_path
        ]
    )
print(total_paths)
