input_file = open("inputd17.txt", "r")
input_lines = input_file.readlines()

import re

total_eggnog = 150
possible_combinations = [1] + total_eggnog * [0]
for line in input_lines:
    container_size = int(line)
    new_combinations = container_size * [0] + possible_combinations
    possible_combinations = list(
        map(sum, zip(new_combinations, possible_combinations))
    )[: total_eggnog + 1]
print(possible_combinations[-1])
