input_file = open('inputd15.txt','r')
input_lines = input_file.readlines()

import re
import operator
import functools

properties = []
for line in input_lines:
  properties.append([int(x) for x in re.findall('-?\d+', line.strip())])
number_of_ingredients = len(properties)
number_of_properties = len(properties[0])

def partitions(expected_sum, expected_length):
  partitions = [[]]
  length = len(partitions[0])
  while length < expected_length - 1:
    new_partitions = []
    for partition in partitions:
      for new_element in range(expected_sum - sum(partition) + 1):
        new_partitions.append(partition + [new_element])
    partitions = new_partitions
    length = len(partitions[0])
  new_partitions = []
  for partition in partitions:
    new_partitions.append(partition + [expected_sum - sum(partition)])
  return new_partitions

number_of_teaspoons = 100
maximal_score = 0
for partition in partitions(number_of_teaspoons, number_of_ingredients):
  cookie_score = functools.reduce(operator.mul, [max(sum([partition[i] * properties[i][j] for i in range(number_of_ingredients)]), 0) for j in range(number_of_properties - 1)], 1)
  maximal_score = max(maximal_score, cookie_score)
print(maximal_score)
