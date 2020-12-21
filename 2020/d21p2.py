import fileinput
import networkx
import re
import collections

input_lines = list(fileinput.input())

possibly_allergen_ingredient = dict()
all_ingredients = collections.defaultdict(lambda: 0)
for line in input_lines:
    ingredient_block, allergen_block = re.findall(
        "(.*)\ \(contains\ (.*)\)", line.strip()
    )[0]
    ingredients = ingredient_block.split(" ")
    allergens = allergen_block.split(", ")
    for allergen in allergens:
        if allergen not in possibly_allergen_ingredient:
            possibly_allergen_ingredient[allergen] = set(ingredients)
        else:
            possibly_allergen_ingredient[allergen] = possibly_allergen_ingredient[
                allergen
            ] & set(ingredients)
    for ingredient in ingredients:
        all_ingredients[ingredient] += 1

allergen_ingredient_possibilities = networkx.Graph()
for allergen, ingredients in possibly_allergen_ingredient.items():
    allergen_ingredient_possibilities.add_edges_from(
        [(allergen, ingredient) for ingredient in ingredients]
    )
allergen_ingredients = networkx.bipartite.maximum_matching(
    allergen_ingredient_possibilities
)


print(
    ",".join(
        [
            allergen_ingredients[allergen]
            for allergen in sorted(possibly_allergen_ingredient.keys())
        ]
    )
)
