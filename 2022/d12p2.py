import fileinput
import networkx
import string

input_lines = list(fileinput.input())

start_location = None
end_location = None
elevation = []
for y, line in enumerate(input_lines):
    row = []
    for x, char in enumerate(line.strip()):
        if char in string.ascii_lowercase:
            row.append(string.ascii_lowercase.index(char))
        elif char == "S":
            start_location = (y, x)
            row.append(0)
        elif char == "E":
            end_location = (y, x)
            row.append(len(string.ascii_lowercase) - 1)
    elevation.append(row)

elevationmapgraph = networkx.DiGraph()
for y in range(len(elevation)):
    for x in range(len(elevation[0])):
        if y > 0 and elevation[y][x] - elevation[y - 1][x] <= 1:
            elevationmapgraph.add_edge((y - 1, x), (y, x))
        if y > 0 and elevation[y - 1][x] - elevation[y][x] <= 1:
            elevationmapgraph.add_edge((y, x), (y - 1, x))
        if x > 0 and elevation[y][x] - elevation[y][x - 1] <= 1:
            elevationmapgraph.add_edge((y, x - 1), (y, x))
        if x > 0 and elevation[y][x - 1] - elevation[y][x] <= 1:
            elevationmapgraph.add_edge((y, x), (y, x - 1))

fewest_steps = float("inf")
for y in range(len(elevation)):
    for x in range(len(elevation[0])):
        if elevation[y][x] == 0 and networkx.has_path(
            elevationmapgraph, source=(y, x), target=end_location
        ):
            fewest_steps = min(
                fewest_steps,
                networkx.shortest_path_length(
                    elevationmapgraph, source=(y, x), target=end_location
                ),
            )
print(fewest_steps)
