import fileinput
import re
import collections
import math

input_lines = list(fileinput.input())

chip_holders = collections.defaultdict(lambda: [])
transfer_rule = dict()
queue = []
for line in input_lines:
    instruction = line.strip()
    if instruction.startswith("value"):
        value = int(re.search(r"^value\ \d+", instruction).group()[6:])
        register = re.search(r"(?:bot|output)\ \d+", instruction).group()
        chip_holders[register].append(value)
        if len(chip_holders[register]) == 2 and register[:3] == "bot":
            queue.append(register)
    if instruction.startswith("bot"):
        source = re.search(r"^bot\ \d+", instruction).group()
        target_low = re.search(r"low\ to\ (?:bot|output)\ \d+", instruction).group()[7:]
        target_high = re.search(r"high\ to\ (?:bot|output)\ \d+", instruction).group()[
            8:
        ]
        transfer_rule[source] = (target_low, target_high)

while len(queue) > 0:
    bot = queue.pop()
    values = chip_holders[bot]
    next_holders = transfer_rule[bot]
    chip_holders[next_holders[0]].append(min(values))
    if len(chip_holders[next_holders[0]]) == 2 and next_holders[0][:3] == "bot":
        queue.append(next_holders[0])
    chip_holders[next_holders[1]].append(max(values))
    if len(chip_holders[next_holders[1]]) == 2 and next_holders[1][:3] == "bot":
        queue.append(next_holders[1])
    chip_holders[bot] = []

print(math.prod([chip_holders["output " + str(index)][0] for index in range(3)]))
