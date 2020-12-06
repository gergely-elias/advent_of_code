import fileinput
import itertools
import math

input_lines = list(fileinput.input())

numbers = [int(line) for line in input_lines]
target_total = 2020
number_of_terms = 2

for terms in itertools.combinations(numbers, number_of_terms):
    if sum(terms) == target_total:
        print(math.prod(terms))
