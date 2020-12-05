input_file = open("inputd14.txt", "r")
input_lines = input_file.readlines()

import re
import networkx
import math


def parse_input(instr):
    amount, chemical = instr.split()
    return (chemical, int(amount))


dependencies = networkx.DiGraph()
for line_index in range(len(input_lines)):
    reaction = list(map(parse_input, re.findall("\d+ [A-Z]+", input_lines[line_index])))
    for input_chemical_index in range(len(reaction) - 1):
        dependencies.add_edge(reaction[input_chemical_index], reaction[-1])

ingredients = {"FUEL": 1}
processed = []
while set(ingredients.keys()) != set(["ORE"]):
    processed_next = processed[:]
    ingredients_next = {}
    for chemical in ingredients:
        if (
            len(
                set(
                    [
                        reaction[1][0]
                        for reaction in dependencies.edges()
                        if reaction[0][0] == chemical
                    ]
                ).difference(processed)
            )
            == 0
        ):
            processed_next.append(chemical)
            for output_chemical, output_amount in [
                reaction[1] for reaction in dependencies.edges()
            ]:
                if output_chemical == chemical:
                    reaction_amount = math.ceil(ingredients[chemical] / output_amount)
            for input_chemical, input_amount in [
                reaction[0]
                for reaction in dependencies.edges()
                if reaction[1][0] == chemical
            ]:
                if input_chemical not in ingredients_next:
                    ingredients_next[input_chemical] = 0
                ingredients_next[input_chemical] += input_amount * reaction_amount
        else:
            if chemical not in ingredients_next:
                ingredients_next[chemical] = 0
            ingredients_next[chemical] += ingredients[chemical]
    ingredients = ingredients_next
    processed = processed_next

print(ingredients["ORE"])
