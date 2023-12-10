import fileinput
import networkx

input_lines = [line.strip() for line in fileinput.input()]
height = len(input_lines)
width = len(input_lines[0])
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

coords_on_loop = networkx.node_connected_component(pipe_map_graph, start_coord)
double_zoom_coords_on_loop = set()
for y in range(height):
    for x in range(width):
        if (
            y > 0
            and (y, x) in coords_on_loop
            and (y - 1, x) in coords_on_loop
            and pipe_map_graph.has_edge((y, x), (y - 1, x))
        ):
            double_zoom_coords_on_loop.update(
                {(2 * y, 2 * x), (2 * y - 1, 2 * x), (2 * y - 2, 2 * x)}
            )
        if (
            x > 0
            and (y, x) in coords_on_loop
            and (y, x - 1) in coords_on_loop
            and pipe_map_graph.has_edge((y, x), (y, x - 1))
        ):
            double_zoom_coords_on_loop.update(
                {(2 * y, 2 * x), (2 * y, 2 * x - 1), (2 * y, 2 * x - 2)}
            )

double_zoom_non_loop_graph = networkx.Graph()
for y in range(-1, 2 * height - 1):
    for x in range(-1, 2 * width - 1):
        if (
            y > -1
            and (y, x) not in double_zoom_coords_on_loop
            and (y - 1, x) not in double_zoom_coords_on_loop
        ):
            double_zoom_non_loop_graph.add_edge((y, x), (y - 1, x))
        if (
            x > -1
            and (y, x) not in double_zoom_coords_on_loop
            and (y, x - 1) not in double_zoom_coords_on_loop
        ):
            double_zoom_non_loop_graph.add_edge((y, x), (y, x - 1))
coords_outside = {
    (y // 2, x // 2)
    for (y, x) in networkx.node_connected_component(
        double_zoom_non_loop_graph, (-1, -1)
    )
    if y % 2 == 0 and x % 2 == 0
}

print(height * width - len(coords_on_loop) - len(coords_outside))
