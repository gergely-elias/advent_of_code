import fileinput
import math

input_lines = list(fileinput.input())

factor1 = int(input_lines[19].strip().split()[1])
factor2 = int(input_lines[20].strip().split()[1])

register_a = 12

print(math.factorial(register_a) + factor1 * factor2)
