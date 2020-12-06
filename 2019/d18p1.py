import fileinput
import collections
import networkx

input_lines = list(fileinput.input())

mazegraph = networkx.Graph()
mazemap = collections.defaultdict(lambda: "#")
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for row_index in range(len(input_lines)):
    line = input_lines[row_index].strip()
    for col_index in range(len(line)):
        mazemap[(row_index, col_index)] = line[col_index]

positions = dict()
door_keys = []
doors = []
for row_index in range((len(input_lines))):
    for col_index in range(len(input_lines[0])):
        if (
            mazemap[(row_index, col_index)] >= "a"
            and mazemap[(row_index, col_index)] <= "z"
        ):
            door_keys.append(mazemap[(row_index, col_index)])
        elif (
            mazemap[(row_index, col_index)] >= "A"
            and mazemap[(row_index, col_index)] <= "Z"
        ):
            doors.append(mazemap[(row_index, col_index)])
important_nodes = "@" + str(door_keys) + str(doors)

for row_index in range((len(input_lines))):
    for col_index in range(len(input_lines[0])):
        cell = (row_index, col_index)
        if mazemap[cell] in important_nodes:
            positions[mazemap[cell]] = cell
        for direction in directions:
            neighbour_cell = tuple(
                [
                    cell_coord + dir_coord
                    for cell_coord, dir_coord in zip(cell, direction)
                ]
            )
            if mazemap[cell] != "#" and mazemap[neighbour_cell] != "#":
                mazegraph.add_edge(cell, neighbour_cell)
key_dependencies = networkx.DiGraph()
for door_key in door_keys:
    prereq_keys = [
        door.lower()
        for door in (
            list(
                set(
                    [
                        mazemap[cell]
                        for cell in networkx.shortest_path(
                            mazegraph, positions["@"], positions[door_key]
                        )
                    ]
                ).intersection(doors)
            )
        )
    ]
    key_dependencies.add_node(door_key)
    for prereq_key in prereq_keys:
        key_dependencies.add_edge(prereq_key, door_key)

distances = networkx.Graph()
new_nodes = [("", "@")]
distances.add_node(new_nodes[0])

while len(new_nodes) > 0:
    recent_nodes = list(new_nodes)[:]
    new_nodes = set()
    for current_node in recent_nodes:
        collected_keys, last_key = current_node
        for letter in door_keys:
            if (
                letter not in collected_keys
                and len(
                    set(networkx.ancestors(key_dependencies, letter)).difference(
                        set(collected_keys)
                    )
                )
                == 0
            ):
                new_node = ("".join(sorted(collected_keys + letter)), letter)
                new_nodes.add(new_node)
                distances.add_edge(
                    current_node,
                    new_node,
                    weight=networkx.shortest_path_length(
                        mazegraph, positions[last_key], positions[letter]
                    ),
                )

min_distance = float("inf")
distance_from_source = networkx.single_source_dijkstra_path_length(distances, ("", "@"))
for node in distance_from_source:
    if set(node[0]) == set(door_keys):
        min_distance = min(min_distance, distance_from_source[node])
print(min_distance)
