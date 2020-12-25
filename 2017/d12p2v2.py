import fileinput
import re

input_lines = list(fileinput.input())

groups = []

for line in input_lines:
    program_ids = set([int(x) for x in re.findall(r"\d+", line.strip())])
    for i, group in reversed(list(enumerate(groups))):
        if len(program_ids.intersection(group)) > 0:
            program_ids.update(group)
            groups.pop(i)
    groups.append(program_ids)

print(len(groups))
