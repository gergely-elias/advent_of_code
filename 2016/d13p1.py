import fileinput
import networkx

input_lines = list(fileinput.input())

designer_number = int(input_lines[0].strip())


def wall(x, y):
    return (
        bin(x * x + 3 * x + 2 * x * y + y + y * y + designer_number)[2:].count("1") % 2
        == 1
    )


source = (1, 1)
target = (31, 39)

maze = networkx.Graph()
diagonal = 0
distance = float("inf")
while 2 * diagonal - sum(source) - sum(target) < distance:
    for x in range(0, diagonal + 1):
        y = diagonal - x
        if not wall(x, y):
            maze.add_node((x, y))
            if (x - 1, y) in maze.nodes():
                maze.add_edge((x, y), (x - 1, y))
            if (x, y - 1) in maze.nodes():
                maze.add_edge((x, y), (x, y - 1))
    if diagonal >= sum(target) and networkx.has_path(maze, source, target):
        distance = min(networkx.shortest_path_length(maze, source, target), distance)
    diagonal += 1
print(distance)
