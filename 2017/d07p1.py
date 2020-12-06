import fileinput
import re

input_lines = list(fileinput.input())

base_discs = set()
subtower_discs = set()

for line in input_lines:
    discs = re.findall("[a-z]+", line)
    base_discs.add(discs[0])
    subtower_discs.update(discs[1:])

print(list(base_discs.difference(subtower_discs))[0])
