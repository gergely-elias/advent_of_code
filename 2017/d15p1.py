import fileinput
import re

input_lines = list(fileinput.input())

values = [int(re.findall(r"\d+", line)[0]) for line in input_lines]
factors = [16807, 48271]
remainder_modulus = 2147483647
digits_to_compare = 16
compare_modulus = 2 ** digits_to_compare

number_of_matches = 0
steps = 40000000
iteration_function = (
    lambda value_factor_pair: value_factor_pair[0]
    * value_factor_pair[1]
    % remainder_modulus
)

for i in range(steps):
    values = [iteration_function(i) for i in zip(values, factors)]
    if values[0] % compare_modulus == values[1] % compare_modulus:
        number_of_matches += 1
print(number_of_matches)
