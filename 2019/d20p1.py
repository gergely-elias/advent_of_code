import fileinput
import re
import collections
import networkx

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
    for y in edge_y:
        for x in edge_x:
            portal_name_coord = (y, x)
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
                if portal_name not in portals:
                    portals[portal_name] = []
                portals[portal_name].append(
                    tuple(
                        [
                            coord - step
                            for (coord, step) in zip(
                                portal_name_coord, edge_normal_direction
                            )
                        ]
                    )
                )

for portal in portals:
    if portal not in ["AA", "ZZ"]:
        maze.add_edge(*portals[portal])
print(networkx.shortest_path_length(maze, *portals["AA"], *portals["ZZ"]))
