import fileinput
import networkx

input_lines = list(fileinput.input())

filesystem_graph = networkx.DiGraph()
root_directory = tuple("/")
filesystem_graph.add_node(root_directory, filesize=0)

for line in input_lines:
    line = line.strip()
    if line == "$ cd /":
        current_directory = root_directory
        filesystem_graph.add_node(current_directory, filesize=0, type="directory")
    elif line == "$ cd ..":
        current_directory = tuple(list(current_directory)[:-1])
    elif line.startswith("$ cd "):
        directory_name = line[5:]
        current_directory = tuple(list(current_directory) + [directory_name])
    elif line == "$ ls":
        pass
    elif line.startswith("dir "):
        directory_name = line[4:]
        node_name = tuple(list(current_directory) + [directory_name])
        filesystem_graph.add_node(node_name, filesize=0, type="directory")
        filesystem_graph.add_edge(current_directory, node_name)
    else:
        file_size, file_name = line.split()
        node_name = tuple(list(current_directory) + [file_name])
        filesystem_graph.add_node(node_name, filesize=int(file_size), type="file")
        filesystem_graph.add_edge(current_directory, node_name)


own_size = networkx.get_node_attributes(filesystem_graph, "filesize")
node_type = networkx.get_node_attributes(filesystem_graph, "type")
total_size = {}

for node in reversed(list(networkx.topological_sort(filesystem_graph))):
    if node_type[node] == "file":
        total_size[node] = own_size[node]
    else:
        total_size[node] = sum(
            total_size[neighbor_node]
            for neighbor_node in filesystem_graph.neighbors(node)
        )


min_size = total_size[root_directory] - 40000000
print(
    min(
        [
            total_size[node]
            for node in filesystem_graph.nodes()
            if node_type[node] == "directory" and total_size[node] >= min_size
        ]
    )
)
