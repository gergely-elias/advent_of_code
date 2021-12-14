import fileinput
import collections

input_lines = list(fileinput.input())

total_steps = 40
polymer_template = input_lines[0].strip()
pair_insertion_rules = {
    element_pair: new_element
    for element_pair, new_element in [
        line.strip().split(" -> ") for line in input_lines[2:]
    ]
}

current_element_pair_counter = collections.Counter(
    [
        polymer_template[element_index : element_index + 2]
        for element_index in range(len(polymer_template) - 1)
    ]
)
for step in range(total_steps):
    next_element_pair_counter = collections.defaultdict(lambda: 0)
    for element_pair in current_element_pair_counter:
        element_to_insert = pair_insertion_rules[element_pair]
        next_element_pair_counter[
            element_pair[0] + element_to_insert
        ] += current_element_pair_counter[element_pair]
        next_element_pair_counter[
            element_to_insert + element_pair[1]
        ] += current_element_pair_counter[element_pair]
    current_element_pair_counter = next_element_pair_counter

element_count = collections.defaultdict(lambda: 0)
for element_pair in current_element_pair_counter:
    element_count[element_pair[0]] += current_element_pair_counter[element_pair]
element_count[polymer_template[-1]] += 1

print(max(element_count.values()) - min(element_count.values()))
