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
en_route_small_caves = [x for x in small_caves if x not in ["start", "end"]]

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
for en_route_small_cave in en_route_small_caves:
    small_cave_reduced_connections.add_edge(
        en_route_small_cave,
        en_route_small_cave,
        weight=sum(
            [
                cave_connections.has_edge(en_route_small_cave, big_cave)
                for big_cave in big_caves
            ]
        ),
    )

valid_en_route_small_cave_paths = set()
for number_of_en_route_small_caves_visited_once in range(len(en_route_small_caves) + 1):
    for caves_visited_once in itertools.combinations(
        en_route_small_caves, number_of_en_route_small_caves_visited_once
    ):
        for en_route_path in itertools.permutations(caves_visited_once):
            valid_en_route_small_cave_paths.add(tuple(en_route_path))
for cave_visited_twice in en_route_small_caves:
    for number_of_en_route_small_caves_visited_once in range(len(en_route_small_caves)):
        for caves_visited_once in itertools.combinations(
            [cave for cave in en_route_small_caves if cave != cave_visited_twice],
            number_of_en_route_small_caves_visited_once,
        ):
            for en_route_path in itertools.permutations(
                caves_visited_once + 2 * (cave_visited_twice,)
            ):
                valid_en_route_small_cave_paths.add(tuple(en_route_path))

total_paths = 0
for en_route_small_cave_path in valid_en_route_small_cave_paths:
    small_cave_edge_path = zip(
        ("start",) + en_route_small_cave_path, en_route_small_cave_path + ("end",)
    )
    total_paths += math.prod(
        [
            small_cave_reduced_connections.get_edge_data(*edge)["weight"]
            for edge in small_cave_edge_path
        ]
    )
print(total_paths)
