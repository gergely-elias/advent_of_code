import fileinput
import networkx

input_lines = list(fileinput.input())
connected_pairs = [line.strip().split("-") for line in input_lines]
network_graph = networkx.Graph()
for pair in connected_pairs:
    network_graph.add_edge(*pair)

largest_clique = []
for clique in networkx.find_cliques(network_graph):
    if len(clique) > len(largest_clique):
        largest_clique = clique
print(",".join((sorted(largest_clique))))
