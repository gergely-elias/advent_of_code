import fileinput
import collections
import networkx
import re

input_lines = list(fileinput.input())

bags = networkx.DiGraph()

for line in input_lines:
    bags_in_bag = re.findall("\w+\ \w+\ bag", line.strip())
    outer_bag = bags_in_bag[0]
    for inner_bag in bags_in_bag[1:]:
        bags.add_edge(outer_bag, inner_bag)

print(len(networkx.ancestors(bags, "shiny gold bag")))
