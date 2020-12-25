import fileinput
import re
import collections
import networkx
import itertools

input_lines = list(fileinput.input())

maze = networkx.Graph()
maze_lines = []
mazemap = collections.defaultdict(lambda: "#")
for line_index in range(len(input_lines)):
    maze_lines.append(input_lines[line_index].strip("\n"))

donut_height_with_portals = len(maze_lines)
donut_height = donut_height_with_portals - 2 * 2
donut_width_with_portals = len(maze_lines[0])
donut_width = donut_width_with_portals - 2 * 2

breadth = donut_width
for line_index in range(2, len(input_lines) - 2):
    breadth = min(
        breadth, min(list(map(len, re.findall(r"[\.#]+", maze_lines[line_index]))))
    )

for y in range(donut_height_with_portals):
    for x in range(donut_width_with_portals):
        mazemap[(y, x)] = maze_lines[y][x]

portals = dict()
for y in range(donut_height_with_portals):
    for x in range(donut_width_with_portals):
        coord = (y, x)
        for step_dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            neighbour_coord = tuple(
                [current + step for (current, step) in zip(coord, step_dir)]
            )
            if mazemap[coord] not in " #" and mazemap[neighbour_coord] not in " #":
                maze.add_edge(coord, neighbour_coord)

donut_edges = [
    ([1, donut_height + 2 - breadth - 1], range(2, donut_width + 2), (-1, 0)),
    ([donut_height + 2, breadth + 2], range(2, donut_width + 2), (1, 0)),
    (range(2, donut_height + 2), [1, donut_width + 2 - breadth - 1], (0, -1)),
    (range(2, donut_height + 2), [donut_width + 2, 2 + breadth], (0, 1)),
]

for edge_y, edge_x, edge_normal_direction in donut_edges:
    for idxy, y in enumerate(edge_y):
        for idxx, x in enumerate(edge_x):
            portal_name_coord = (y, x)
            inner_ridge = [idxx, idxy][edge_normal_direction.index(0)] == 1
            if mazemap[portal_name_coord] not in " #.":
                portal_name = (
                    mazemap[
                        tuple(
                            [
                                coord + step
                                for (coord, step) in zip(
                                    portal_name_coord, edge_normal_direction
                                )
                            ]
                        )
                    ]
                    + mazemap[(y, x)]
                )
                if sum(edge_normal_direction) == 1:
                    portal_name = "".join(reversed(portal_name))
                if inner_ridge:
                    portal_name += "+"
                portals[portal_name] = tuple(
                    [
                        coord - step
                        for (coord, step) in zip(
                            portal_name_coord, edge_normal_direction
                        )
                    ]
                )

connected_portals = dict()
for portalpair in itertools.combinations(portals, 2):
    if networkx.has_path(maze, *[portals[portal] for portal in portalpair]):
        connected_portals[portalpair] = networkx.shortest_path_length(
            maze, *[portals[portal] for portal in portalpair]
        )


def portal_with_layer(portal_name, layer):
    return portal_name[:2] + str(layer + (1 if portal_name.endswith("+") else 0))


multilayer_maze = networkx.Graph()
min_distance = float("inf")
layer = 0
while (2 * layer + 1) * (min(connected_portals.values()) + 1) - 1 < min_distance:
    for edge in connected_portals:
        multilayer_maze.add_edge(
            portal_with_layer(edge[0], layer),
            portal_with_layer(edge[1], layer),
            weight=connected_portals[edge] + 1,
        )
    if networkx.has_path(multilayer_maze, "AA0", "ZZ0"):
        min_distance = (
            networkx.shortest_path_length(
                multilayer_maze, "AA0", "ZZ0", weight="weight"
            )
            - 1
        )
    layer += 1
print(min_distance)
