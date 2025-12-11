import fileinput
import networkx

input_lines = list(fileinput.input())

network = networkx.DiGraph()
for line in input_lines:
    device, outputs_raw = line.strip().split(":")
    outputs = outputs_raw.split(" ")
    for output in outputs:
        network.add_edge(device, output)

print(len(list(networkx.all_simple_paths(network, "you", "out"))))
