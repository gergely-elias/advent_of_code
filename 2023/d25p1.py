import fileinput
import math
import networkx
import re

input_lines = list(fileinput.input())
wires = networkx.Graph()
for line in input_lines:
    components = re.findall(r"\w+", line.strip())
    source_component = components[0]
    target_components = components[1:]
    for target_component in target_components:
        wires.add_edge(source_component, target_component)

groups = list(networkx.k_edge_components(wires, 3 + 1))
print(math.prod(len(group) for group in groups))
