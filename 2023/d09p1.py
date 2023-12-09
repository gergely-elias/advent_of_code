import fileinput
import re

input_lines = list(fileinput.input())
sum_of_extrapolated_next_values = 0
for line in input_lines:
    value_history = list(map(int, re.findall(r"-?\d+", line.strip())))
    difference_sequence = value_history
    difference_coefficients = []
    while any(difference_sequence):
        difference_coefficients.append(difference_sequence[-1])
        difference_sequence = [
            a - b for a, b in zip(difference_sequence[1:], difference_sequence[:-1])
        ]
    sum_of_extrapolated_next_values += sum(difference_coefficients)
print(sum_of_extrapolated_next_values)
