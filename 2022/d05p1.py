import fileinput
import re

input_lines = list(fileinput.input())

separator_line_index = input_lines.index("\n")

initial_crates_lines = input_lines[:separator_line_index]

number_of_crate_stacks = (len(initial_crates_lines[-2].strip()) + 1) // 4
stacks = [[] for _ in range(number_of_crate_stacks)]
for line in initial_crates_lines[:-1]:
    for stack_index in range(number_of_crate_stacks):
        crate = line[stack_index * 4 + 1]
        if crate != " ":
            stacks[stack_index].append(crate)

for line in input_lines[separator_line_index + 1 :]:
    x, y, z = map(int, re.findall(r"\d+", line.strip()))
    stacks[z - 1] = list(reversed(stacks[y - 1][:x])) + stacks[z - 1]
    stacks[y - 1] = stacks[y - 1][x:]

print("".join([stack[0] for stack in stacks]))
