import fileinput
import re

input_lines = list(fileinput.input())

memory = dict()
for line in input_lines:
    line = line.strip()
    if line[:4] == "mask":
        mask = line[7:]
        ones = int(mask.replace("X", "1"), 2)
        zeros = int(mask.replace("X", "0"), 2)
    else:
        address, value = map(int, re.findall(r"\d+", line))
        memory[address] = (value & ones) | zeros
print(sum(memory.values()))
