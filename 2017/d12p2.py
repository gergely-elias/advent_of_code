import fileinput
import re

input_lines = list(fileinput.input())

neighbours = []
for line in input_lines:
    neighbours.append([int(x) for x in re.findall("\d+", line.strip())][1:])

group = set()
remaining_ids = set(range(len(neighbours)))
connected = set()
number_of_groups = 0

while len(remaining_ids) > 0:
    connected = set([list(remaining_ids)[0]])
    while len(connected) > 0:
        program_id = list(connected)[0]
        connected.remove(program_id)
        remaining_ids.remove(program_id)
        group.add(program_id)
        for neighbour in neighbours[program_id]:
            if neighbour not in group and neighbour not in connected:
                connected.add(neighbour)
    number_of_groups += 1

print(number_of_groups)
