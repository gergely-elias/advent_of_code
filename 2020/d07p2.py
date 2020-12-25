import fileinput
import networkx
import re

input_lines = list(fileinput.input())

bags = networkx.DiGraph()

for line in input_lines:
    bags_in_bag = re.findall(r"(?:(\d+)\ )?(\w+\ \w+\ bag)", line.strip())
    outer_bag = bags_in_bag[0]
    for inner_bag in bags_in_bag[1:]:
        bags.add_edge(
            outer_bag[1],
            inner_bag[1],
            weight=(0 if inner_bag[0] == "" else int(inner_bag[0])),
        )

target_bag = "shiny gold bag"
number_of_bags_inside = dict()

bags_inside_target_bag = [
    bag
    for bag in reversed(list(networkx.topological_sort(bags)))
    if bag in networkx.descendants(bags, target_bag).union([target_bag])
]

for bag in bags_inside_target_bag:
    bags_inside_current_bag = 0
    for outer_bag, inner_bag, edge_data in bags.out_edges(bag, data=True):
        bags_inside_current_bag += edge_data["weight"] * (
            1 + number_of_bags_inside[inner_bag]
        )
    number_of_bags_inside[bag] = bags_inside_current_bag
print(number_of_bags_inside[target_bag])
