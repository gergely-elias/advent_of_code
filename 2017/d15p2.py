input_file = open('inputd15.txt','r')
input_lines = input_file.readlines()

import re

values = [int(re.findall('\d+', line)[0]) for line in input_lines]
factors = [16807, 48271]
remainder_modulus = 2147483647
digits_to_compare = 16
compare_modulus = 2 ** digits_to_compare

number_of_matches = 0
steps = 5000000
iteration_function = lambda (value, factor): value * factor % remainder_modulus
mandatory_divisor = [4, 8]

for step in range(steps):
  values = [iteration_function(i) for i in zip(values, factors)]
  for i,value in enumerate(values):
    while value % mandatory_divisor[i] != 0:
      value = iteration_function((value, factors[i]))
    values[i] = value

  if values[0] % compare_modulus == values[1] % compare_modulus:
    number_of_matches += 1
print number_of_matches
