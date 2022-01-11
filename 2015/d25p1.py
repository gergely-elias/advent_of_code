import fileinput
import re

input_lines = list(fileinput.input())

[row, column] = map(int, re.findall(r"\d+", input_lines[0].strip()))
previous_diagonal_max = (row + column - 2) * (row + column - 1) // 2
index = previous_diagonal_max + column - 1

start = 20151125
base = 252533
modulus = 33554393

print(pow(base, index, modulus) * start % modulus)
