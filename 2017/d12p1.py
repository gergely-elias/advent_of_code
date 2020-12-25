import fileinput
import re

input_lines = list(fileinput.input())

neighbours = []
for line in input_lines:
    neighbours.append([int(x) for x in re.findall(r"\d+", line.strip())][1:])

group = set()
remaining_ids = set(range(len(neighbours)))
connected = set([0])

while len(connected) > 0:
    program_id = list(connected)[0]
    connected.remove(program_id)
    remaining_ids.remove(program_id)
    group.add(program_id)
    for neighbour in neighbours[program_id]:
        if neighbour not in group and neighbour not in connected:
            connected.add(neighbour)

print(len(group))
