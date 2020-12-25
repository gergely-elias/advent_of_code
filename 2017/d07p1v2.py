import fileinput
import re

input_lines = list(fileinput.input())

discs = re.findall(r"[a-z]+", "".join(input_lines))

unique_discs = set()
for disc in discs:
    unique_discs.symmetric_difference_update(set([disc]))

print(list(unique_discs)[0])
