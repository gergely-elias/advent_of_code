import fileinput
import networkx

input_lines = list(fileinput.input())

orbit_graph = networkx.Graph()
for line_index in range(len(input_lines)):
    orbit_graph.add_edge(*input_lines[line_index].strip().split(")"))

source = "YOU"
target = "SAN"
print(networkx.shortest_path_length(orbit_graph, source, target) - 2)
