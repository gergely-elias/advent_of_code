input_file = open("inputd20.txt", "r")
input_lines = input_file.readlines()

import sympy

divisor_sum_threshold = int(input_lines[0]) // 10
candidate = 1
while sum(sympy.divisors(candidate)) < divisor_sum_threshold:
    candidate += 1
print(candidate)
