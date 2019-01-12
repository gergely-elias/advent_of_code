input_file = open('inputd08.txt','r')
input_lines = input_file.readlines()

import collections

registers = collections.defaultdict(lambda: 0)
maximal_register = float("-inf")
for line in input_lines:
  expression = line.split(' ')
  register_to_modify = expression[0]
  increment = int(expression[2])*(1 if expression[1]=="inc" else -1)
  register_in_condition = expression[4]
  condition = 'registers["' + register_in_condition + '"]' + expression[5] + expression[6]

  if eval(condition):
    registers[register_to_modify] += increment

  for register in registers:
    if registers[register] > maximal_register:
      maximal_register = registers[register]
print(maximal_register)
