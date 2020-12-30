import fileinput
import re
import math

input_lines = list(fileinput.input())

discs = []
for line in input_lines:
    discs.append(map(int, re.findall(r"\d+", line.strip())))
discs.append((len(discs) + 1, 11, 0, 0))

time = 0
step = 1
for disc_index, position_count, initial_time, initial_position in discs:
    assert math.gcd(step, position_count) == 1
    while (time + disc_index + initial_position - initial_time) % position_count != 0:
        time += step
    step *= position_count
print(time)
