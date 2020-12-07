import fileinput
import collections
import networkx
import re

input_lines = list(fileinput.input())

bags = networkx.DiGraph()

for line in input_lines:
    bags_in_bag = re.findall("(?:(\d+)\ )?(\w+\ \w+\ bag)", line.strip())
    outer_bag = bags_in_bag[0]
    for inner_bag in bags_in_bag[1:]:
        bags.add_edge(
            outer_bag[1],
            inner_bag[1],
            weight=(0 if inner_bag[0] == "" else int(inner_bag[0])),
        )

number_of_bags_inside = dict()
for bag in reversed(list(networkx.topological_sort(bags))):
    bags_inside_current_bag = 0
    for outer_bag, inner_bag, edge_data in bags.out_edges(bag, data=True):
        bags_inside_current_bag += edge_data["weight"] * (
            1 + number_of_bags_inside[inner_bag]
        )
    if bag == "shiny gold bag":
        print(bags_inside_current_bag)
        exit()
    number_of_bags_inside[bag] = bags_inside_current_bag
