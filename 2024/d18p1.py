import fileinput
import networkx

input_lines = list(fileinput.input())
fall_order = [tuple(map(int, line.strip().split(","))) for line in input_lines]
width = 71
height = 71

memory_grid = networkx.Graph()
for x in range(width):
    for y in range(height):
        if x > 0:
            memory_grid.add_edge((x, y), (x - 1, y))
        if y > 0:
            memory_grid.add_edge((x, y), (x, y - 1))

for falling_byte in fall_order[:1024]:
    memory_grid.remove_node(falling_byte)

startpos = (0, 0)
endpos = (width - 1, height - 1)

print(networkx.shortest_path_length(memory_grid, startpos, endpos))
