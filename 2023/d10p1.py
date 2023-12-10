import fileinput
import networkx

input_lines = [line.strip() for line in fileinput.input()]
pipe_map_dict = {}
for line_index, line in enumerate(input_lines):
    for char_index, char in enumerate(line):
        pipe_map_dict[(line_index, char_index)] = char

directions_by_piece = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(1, 0), (-1, 0), (0, 1), (0, -1)],
}


def tuple_sum(*t):
    return tuple(sum(coords) for coords in zip(*t))


def tuple_opposite(t):
    return tuple(-coord for coord in t)


pipe_map_graph = networkx.Graph()
for coords, pipe in pipe_map_dict.items():
    for neighbour_direction in directions_by_piece[pipe]:
        neighbour_coords = tuple_sum(coords, neighbour_direction)
        neighbour_pipe = (
            pipe_map_dict[neighbour_coords]
            if neighbour_coords in pipe_map_dict
            else "."
        )
        neighbour_pipe_directions = directions_by_piece[neighbour_pipe]
        if tuple_opposite(neighbour_direction) in neighbour_pipe_directions:
            pipe_map_graph.add_edge(coords, neighbour_coords)
    if pipe == "S":
        start_coord = coords

print(
    max(
        networkx.single_source_dijkstra_path_length(
            pipe_map_graph, start_coord
        ).values()
    )
)
