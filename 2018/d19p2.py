input_file = open('inputd19.txt','r')
input_lines = input_file.readlines()

import re
import collections

instruction_lines = [input_lines[line_index].strip() for line_index in range(1, len(input_lines))]
variables = [int(re.findall('-?\d+', instruction_line)[1]) for instruction_line in instruction_lines]

number_to_factorize = variables[17] ** 2 * 19 * variables[20] + variables[21] * 22 + variables[23] + (27 * 28 + 29) * 30 * variables[31] * 32

factors = collections.defaultdict(lambda: 0)
possible_prime_divisor = 2
while possible_prime_divisor ** 2 <= number_to_factorize:
  while number_to_factorize % possible_prime_divisor == 0:
    number_to_factorize /= possible_prime_divisor
    factors[possible_prime_divisor] += 1 
  possible_prime_divisor += 1
if number_to_factorize > 1:
  factors[number_to_factorize] += 1

sum_of_divisors = 1
for prime_factor in factors:
  sum_of_divisors *= (prime_factor ** (factors[prime_factor] + 1) - 1) / (prime_factor - 1)
print sum_of_divisors
