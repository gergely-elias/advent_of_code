input_file = open("inputd17.txt", "r")
input_lines = input_file.readlines()

import copy
import re

number_of_containers = len(input_lines)
total_eggnog = 150
possible_combinations = [[1] + [0 for i in range(number_of_containers)]] + [
    [0 for i in range(number_of_containers + 1)] for j in range(total_eggnog)
]

for line in input_lines:
    container_size = int(line)
    new_combinations = [
        [0 for i in range(number_of_containers + 1)] for j in range(container_size)
    ] + [
        [0] + [x for x in i[:number_of_containers]]
        for i in possible_combinations[: total_eggnog + 1 - container_size]
    ]

    possible_combinations = [
        list(map(sum, zip(i[0], i[1])))
        for i in zip(new_combinations, possible_combinations)
    ]

for i in possible_combinations[total_eggnog]:
    if i > 0:
        print(i)
        break
