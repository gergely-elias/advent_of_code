input_file = open("inputd20.txt", "r")
input_lines = input_file.readlines()

import networkx
import re


def process_literals(route_regexp, start_nodes):
    finish_nodes = []
    for node in start_nodes:
        character_index = 0
        while character_index < len(route_regexp):
            character = route_regexp[character_index]
            if character in direction_letters:
                direction = direction_coords[direction_letters.index(character)]
                neighbour_node = tuple(sum(coord) for coord in zip(direction, node))
                rooms.add_edge(node, neighbour_node)
                node = neighbour_node
                character_index += 1
        finish_nodes.append(node)
    return finish_nodes


def preprocess_first_parenthesis(route_regexp, nodes):
    first_parenthesis_start = route_regexp.find("(")
    if first_parenthesis_start > -1:
        number_of_open_parentheses = 1
        character_index = first_parenthesis_start + 1
        while number_of_open_parentheses > 0:
            character = route_regexp[character_index]
            if character == "(":
                number_of_open_parentheses += 1
            elif character == ")":
                number_of_open_parentheses -= 1
            character_index += 1
        first_parenthesis_end = character_index - 1
        next_nodes = process_literals(route_regexp[:first_parenthesis_start], nodes)
        next_nodes = split_on_the_highest_level(
            route_regexp[first_parenthesis_start + 1 : first_parenthesis_end],
            next_nodes,
        )
        return preprocess_first_parenthesis(
            route_regexp[first_parenthesis_end + 1 :], next_nodes
        )
    else:
        return process_literals(route_regexp, nodes)


def split_on_the_highest_level(route_regexp, nodes):
    number_of_open_parentheses = 0
    character_index = 0
    split_result = []
    buffer = ""
    while character_index < len(route_regexp):
        next_char = route_regexp[character_index]
        if next_char == "|" and number_of_open_parentheses == 0:
            split_result.append(buffer)
            buffer = ""
        else:
            buffer += next_char
            if next_char == "(":
                number_of_open_parentheses += 1
            elif next_char == ")":
                number_of_open_parentheses -= 1
        character_index += 1
    split_result.append(buffer)
    next_nodes = set()
    for sub_regexp in split_result:
        next_nodes.update(preprocess_first_parenthesis(sub_regexp, nodes))
    return list(next_nodes)


start_node = (0, 0)
rooms = networkx.Graph()
direction_letters = ["N", "E", "S", "W"]
direction_coords = [(-1, 0), (0, 1), (1, 0), (0, -1)]

split_on_the_highest_level(input_lines[0].strip()[1:-1], [start_node])
print(max(networkx.shortest_path_length(rooms, source=start_node).values()))
