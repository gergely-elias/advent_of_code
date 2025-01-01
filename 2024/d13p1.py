import fileinput
import math
import re

input_lines = list(fileinput.input())
input_line_blocks = list(
    map(lambda x: x.split("\n"), "".join(input_lines).strip().split("\n\n"))
)

a_cost = 3
b_cost = 1

total_cost = 0
for block_lines in input_line_blocks:
    a_x, a_y = map(int, re.findall(r"-?\d+", block_lines[0]))
    b_x, b_y = map(int, re.findall(r"-?\d+", block_lines[1]))
    p_x, p_y = map(int, re.findall(r"-?\d+", block_lines[2]))
    min_cost = math.inf
    for a_count in range(100):
        b_count = (p_x - a_x * a_count) // b_x
        if (
            a_x * a_count + b_x * b_count == p_x
            and a_y * a_count + b_y * b_count == p_y
        ):
            current_cost = a_cost * a_count + b_cost * b_count
            min_cost = min(min_cost, current_cost)
    if min_cost < math.inf:
        total_cost += min_cost
print(total_cost)
