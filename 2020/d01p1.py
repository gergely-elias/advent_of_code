input_file = open('inputd01.txt','r')
input_lines = input_file.readlines()

import itertools
import math

numbers = [int(line) for line in input_lines]
target_total = 2020
number_of_terms = 2

for terms in itertools.combinations(numbers, number_of_terms):
  if sum(terms) == target_total:
    print(math.prod(terms))
