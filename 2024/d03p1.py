import fileinput
import math
import re

concatenated_input_lines = "".join(line.strip() for line in fileinput.input())
multiplications = re.findall(r"mul\((\d+),(\d+)\)", concatenated_input_lines)

print(sum(math.prod(map(int, m)) for m in multiplications))
