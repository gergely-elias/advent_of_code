import fileinput
import copy
import collections

input_lines = list(fileinput.input())

landscape = collections.defaultdict(lambda: -1)
area_size = len(input_lines)

for y in range(area_size):
    line = input_lines[y].strip()
    for x in range(area_size):
        landscape[y, x] = [".", "|", "#"].index(line[x])

target_minute = 10
current_minute = 0
while current_minute < target_minute:
    next_landscape = copy.deepcopy(landscape)
    for y in range(area_size):
        for x in range(area_size):
            neighbourhood = [
                landscape[neighbour_y, neighbour_x]
                for neighbour_x in range(x - 1, x + 2)
                for neighbour_y in range(y - 1, y + 2)
            ]
            if landscape[y, x] == 0 and neighbourhood.count(1) >= 3:
                next_landscape[y, x] = 1
            elif landscape[y, x] == 1 and neighbourhood.count(2) >= 3:
                next_landscape[y, x] = 2
            elif landscape[y, x] == 2 and (
                neighbourhood.count(2) < 2 or neighbourhood.count(1) < 1
            ):
                next_landscape[y, x] = 0
    landscape = next_landscape
    current_minute += 1

print(list(landscape.values()).count(1) * list(landscape.values()).count(2))
