import fileinput
import networkx

input_lines = list(fileinput.input())
connected_pairs = [line.strip().split("-") for line in input_lines]
network_graph = networkx.Graph()
for pair in connected_pairs:
    network_graph.add_edge(*pair)

possible_lan_parties = set()
chief_candidates = [node for node in network_graph.nodes() if node.startswith("t")]
for chief_candidate in chief_candidates:
    for other_participants in network_graph.edges():
        if chief_candidate not in other_participants and all(
            network_graph.has_edge(chief_candidate, other)
            for other in other_participants
        ):
            possible_lan_parties.add(frozenset((chief_candidate,) + other_participants))
print(len(possible_lan_parties))
