import fileinput
import collections

input_lines = list(fileinput.input())

total_steps = 10
polymer_template = input_lines[0].strip()
pair_insertion_rules = {
    element_pair: new_element
    for element_pair, new_element in [
        line.strip().split(" -> ") for line in input_lines[2:]
    ]
}

current_polymer = polymer_template
for step in range(total_steps):
    next_polymer = ""
    for element_index in range(len(current_polymer) - 1):
        element_pair = current_polymer[element_index : element_index + 2]
        next_polymer += (
            current_polymer[element_index] + pair_insertion_rules[element_pair]
        )
    next_polymer += polymer_template[-1]
    current_polymer = next_polymer

element_count = collections.Counter(current_polymer).values()

print(max(element_count) - min(element_count))
