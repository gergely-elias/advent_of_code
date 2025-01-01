import fileinput
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
    p_x, p_y = map(
        lambda n: int(n) + 10000000000000, re.findall(r"-?\d+", block_lines[2])
    )

    assert a_y * b_x - a_x * b_y
    if (a_y * p_x - a_x * p_y) % (a_y * b_x - a_x * b_y):
        continue
    b_count = (a_y * p_x - a_x * p_y) // (a_y * b_x - a_x * b_y)
    a_count = (b_y * p_x - b_x * p_y) // (b_y * a_x - b_x * a_y)
    total_cost += a_cost * a_count + b_cost * b_count

print(total_cost)
