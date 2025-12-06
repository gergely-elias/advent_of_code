import fileinput
import networkx

input_lines = list(fileinput.input())
grid = [line.strip() for line in input_lines]
NEIGHBOUR_DIRECTIONS = {
    (y, x) for y in range(-1, 2) for x in range(-1, 2) if (x, y) != (0, 0)
}

grid_graph = networkx.Graph()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@":
            grid_graph.add_node((y, x))
            for direction in NEIGHBOUR_DIRECTIONS:
                neighbour = tuple(sum(coords) for coords in zip((y, x), direction))
                if grid_graph.has_node(neighbour):
                    grid_graph.add_edge(neighbour, (y, x))

orig_num_of_nodes = len(grid_graph.nodes())
nodes_to_remove = [n for n in grid_graph.nodes() if grid_graph.degree(n) < 4]
grid_graph.remove_nodes_from(nodes_to_remove)
print(orig_num_of_nodes - len(grid_graph.nodes()))
