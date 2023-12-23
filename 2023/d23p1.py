import fileinput
import networkx

input_lines = list(fileinput.input())

garden = [row.strip() for row in input_lines]
height = len(garden)
width = len(garden[0])
source = (0, garden[0].index("."))
target = (height - 1, garden[-1].index("."))

garden_graph = networkx.DiGraph()
for y, row in enumerate(garden):
    for x, cell in enumerate(row):
        if cell != "#":
            if y > 0 and garden[y - 1][x] in [".", "v"]:
                garden_graph.add_edge((y - 1, x), (y, x))
            if y < height - 1 and garden[y + 1][x] in [".", "^"]:
                garden_graph.add_edge((y + 1, x), (y, x))
            if x > 0 and row[x - 1] in [".", ">"]:
                garden_graph.add_edge((y, x - 1), (y, x))
            if x < width - 1 and row[x + 1] in [".", "<"]:
                garden_graph.add_edge((y, x + 1), (y, x))

print(
    max(len(path) for path in networkx.all_simple_paths(garden_graph, source, target))
    - 1
)
