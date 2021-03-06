import fileinput
import re

input_lines = list(fileinput.input())

initial_state = "..." + re.findall(r"[#\.]+", input_lines[0].strip())[0] + "..."

transformations = dict()
for line in input_lines[2:]:
    neighbourhood, new_state = re.findall(r"[#\.]+", line.strip())
    transformations[neighbourhood] = new_state

generation = 20
index_offset = -1
state = initial_state
for step in range(generation):
    plant_index_sum = 0
    next_state = "..."
    for pot_index in range(len(state) - 4):
        next_pot = transformations[state[pot_index : pot_index + 5]]
        if next_pot == "#":
            plant_index_sum += pot_index + index_offset
        next_state += next_pot
    next_state += "..."
    while next_state[-4:] == "....":
        next_state = next_state[:-1]
    while next_state[:4] == "....":
        next_state = next_state[1:]
        index_offset += 1
    state = next_state
    index_offset -= 1
print(plant_index_sum)
