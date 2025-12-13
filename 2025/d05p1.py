import fileinput

input_lines = list(fileinput.input())
interval_block, ingredient_block = "".join(input_lines).split("\n\n")

fresh_intervals = [
    tuple(map(int, line.strip().split("-")))
    for line in interval_block.strip().split("\n")
]
ingredient = [int(line.strip()) for line in ingredient_block.strip().split("\n")]

number_of_fresh_ingredients = 0
for ingredient in ingredient:
    ingredient_is_fresh = False
    for interval_start, interval_end in fresh_intervals:
        if interval_start <= ingredient <= interval_end:
            ingredient_is_fresh = True
            break
    if ingredient_is_fresh:
        number_of_fresh_ingredients += 1
print(number_of_fresh_ingredients)
