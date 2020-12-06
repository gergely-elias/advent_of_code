import fileinput
import re
import networkx
import math

input_lines = list(fileinput.input())


def parse_input(instr):
    amount, chemical = instr.split()
    return (chemical, int(amount))


dependencies = networkx.DiGraph()
reaction_amounts = {}
for line_index in range(len(input_lines)):
    reaction = list(map(parse_input, re.findall("\d+ [A-Z]+", input_lines[line_index])))
    output_chemical, output_chemical_amount = reaction[-1]
    reaction_amount = {output_chemical: output_chemical_amount}
    for input_chemical_index in range(len(reaction) - 1):
        input_chemical, input_chemical_amount = reaction[input_chemical_index]
        dependencies.add_edge(input_chemical, output_chemical)
        reaction_amount[input_chemical] = input_chemical_amount
    reaction_amounts[output_chemical] = reaction_amount

ingredients = {"FUEL": 1}
chemicals = list(networkx.topological_sort(dependencies))
while len(chemicals):
    chemical = chemicals.pop()
    for input_chemical in dependencies.predecessors(chemical):
        if input_chemical not in ingredients:
            ingredients[input_chemical] = 0
        ingredients[input_chemical] += (
            math.ceil(ingredients[chemical] / reaction_amounts[chemical][chemical])
            * reaction_amounts[chemical][input_chemical]
        )

print(ingredients["ORE"])
