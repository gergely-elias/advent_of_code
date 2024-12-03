import fileinput
import math
import re

total = 0
concatenated_input_lines = "".join(line.strip() for line in fileinput.input())
enabled_sections = re.findall(
    r"do\(\)(.*?)don't\(\)", "do()" + concatenated_input_lines + "don't()"
)
for section in enabled_sections:
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", section)
    total += sum(math.prod(map(int, m)) for m in multiplications)
print(total)
