import fileinput
import itertools
import networkx

input_lines = list(fileinput.input())
maze = [line.strip() for line in input_lines]
height = len(maze)
width = len(maze[0])

cheat_length = 2
cheat_count = 0
maze_graph = networkx.Graph()
for y in range(height):
    for x in range(width):
        if y > 0:
            if maze[y][x] != "#" and maze[y - 1][x] != "#":
                maze_graph.add_edge((y, x), (y - 1, x))
        if x > 0:
            if maze[y][x] != "#" and maze[y][x - 1] != "#":
                maze_graph.add_edge((y, x), (y, x - 1))
        if maze[y][x] == "S":
            start_position = (y, x)
        if maze[y][x] == "E":
            finish_position = (y, x)
track_length = networkx.shortest_path_length(
    maze_graph, start_position, finish_position
)
distances_from_start = dict(
    networkx.single_source_shortest_path_length(maze_graph, start_position)
)
distances_to_finish = dict(
    networkx.single_source_shortest_path_length(maze_graph, finish_position)
)
cheat_patterns = [
    (y, x)
    for (y, x) in itertools.product(range(-cheat_length, cheat_length + 1), repeat=2)
    if abs(y) + abs(x) == cheat_length
]
for cheat_start in maze_graph.nodes():
    for cheat_pattern in cheat_patterns:
        cheat_finish = tuple(sum(z) for z in zip(cheat_start, cheat_pattern))
        if cheat_finish in maze_graph.nodes():
            cut_track_length = (
                sum(abs(z) for z in cheat_pattern)
                + distances_from_start[cheat_start]
                + distances_to_finish[cheat_finish]
            )
            if track_length - cut_track_length >= 100:
                cheat_count += 1
print(cheat_count)
