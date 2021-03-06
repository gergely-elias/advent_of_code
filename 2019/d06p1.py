import fileinput
import networkx

input_lines = list(fileinput.input())

orbit_graph = networkx.Graph()
for line_index in range(len(input_lines)):
    orbit_graph.add_edge(*input_lines[line_index].strip().split(")"))

source = "COM"
orbits = networkx.single_source_shortest_path_length(orbit_graph, source)
print(sum(orbits.values()))
