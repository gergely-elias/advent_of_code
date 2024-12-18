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

startpos = (0, 0)
endpos = (width - 1, height - 1)

current_path = networkx.shortest_path(memory_grid, startpos, endpos)
while True:
    falling_byte = fall_order.pop(0)
    memory_grid.remove_node(falling_byte)
    if falling_byte in current_path:
        try:
            current_path = networkx.shortest_path(memory_grid, startpos, endpos)
        except networkx.NetworkXNoPath:
            break
print(",".join(map(str, falling_byte)))
