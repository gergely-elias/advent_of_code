input_file = open("inputd13.txt", "r")
input_lines = input_file.readlines()

import itertools
import collections

happiness_relations = collections.defaultdict(lambda: 0)
people = set()

for line in input_lines:
    words = line.strip().split(" ")
    happiness_value = int(words[3]) * (-1 if words[2] == "lose" else 1)
    pair = (words[0], words[10].strip("."))
    happiness_relations[pair] = happiness_value
    people.update(set(pair))

maximal_happiness = float("-inf")
for sitting_order in itertools.permutations(people):
    current_happiness = 0
    for seat_index in list(range(len(sitting_order) - 1)):
        current_happiness += (
            happiness_relations[
                (
                    sitting_order[seat_index],
                    sitting_order[(seat_index + 1) % len(people)],
                )
            ]
            + happiness_relations[
                (
                    sitting_order[(seat_index + 1) % len(people)],
                    sitting_order[seat_index],
                )
            ]
        )
    if current_happiness > maximal_happiness:
        maximal_happiness = current_happiness
print(maximal_happiness)
