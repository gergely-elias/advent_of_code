import fileinput
import networkx
import itertools

input_lines = list(fileinput.input())

maze = networkx.Graph()
numbers = dict()
for line_index, line in enumerate(input_lines[:-1]):
    for char_index, char in enumerate(line.strip()):
        if char != "#":
            maze.add_node((char_index, line_index))
            if (char_index, line_index - 1) in maze.nodes():
                maze.add_edge((char_index, line_index - 1), (char_index, line_index))
            if (char_index - 1, line_index) in maze.nodes():
                maze.add_edge((char_index - 1, line_index), (char_index, line_index))
            if char != ".":
                numbers[int(char)] = (char_index, line_index)
number_pair_distances = dict()
for number_pair in itertools.combinations(numbers.keys(), 2):
    number_pair_distances[
        tuple(sorted(list(number_pair)))
    ] = networkx.shortest_path_length(
        maze, *[numbers[number] for number in number_pair]
    )
shortest_distance = float("inf")
for numbers_permutation in itertools.permutations(set(numbers.keys()).difference({0})):
    numbers_order = [0] + list(numbers_permutation) + [0]
    order_distance = 0
    for order_index in range(len(numbers_order) - 1):
        order_distance += number_pair_distances[
            tuple(sorted(numbers_order[order_index : order_index + 2]))
        ]
    shortest_distance = min(shortest_distance, order_distance)
print(shortest_distance)
