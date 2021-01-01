import fileinput
import re
import itertools
import networkx
import heapq

input_lines = list(fileinput.input())

nodes = [tuple(map(int, re.findall(r"\d+", line.strip()))) for line in input_lines[2:]]

compatible_pairs = [
    (node_a, node_b)
    for node_a, node_b in itertools.permutations(nodes, 2)
    if node_a[3] <= node_b[2]
]

empty_nodes = [node for node in nodes if node[3] == 0]
assert len(empty_nodes) == 1

empty_node = empty_nodes[0]

compatibility = networkx.DiGraph()
for pair in compatible_pairs:
    compatibility.add_edge(*pair)
moveable_nodes = networkx.ancestors(compatibility, empty_node)
moveable_subgraph = compatibility.subgraph(moveable_nodes)
assert len(moveable_nodes) * (len(moveable_nodes) - 1) == len(moveable_subgraph.edges())

moveable_node_coordinates = set(tuple(node[:2]) for node in moveable_nodes)
target_node = (0, 0)
data_node = (max([node[0] for node in moveable_nodes]), 0)

seen_states = set()
heap_entry_id = 0
states = [(0, heap_entry_id, (data_node, empty_node[:2]))]
heap_entry_id += 1

while len(states) > 0:
    steps_made, _, state = heapq.heappop(states)
    if state in seen_states:
        continue
    seen_states.add(state)
    current_data_node, current_empty_node = state
    if current_data_node == target_node:
        print(steps_made)
        break
    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        empty_neighbour = (
            current_empty_node[0] + direction[0],
            current_empty_node[1] + direction[1],
        )
        if empty_neighbour in moveable_node_coordinates:
            if empty_neighbour == current_data_node:
                heapq.heappush(
                    states,
                    (
                        steps_made + 1,
                        heap_entry_id,
                        (current_empty_node, empty_neighbour),
                    ),
                )
            else:
                heapq.heappush(
                    states,
                    (
                        steps_made + 1,
                        heap_entry_id,
                        (current_data_node, empty_neighbour),
                    ),
                )
            heap_entry_id += 1
