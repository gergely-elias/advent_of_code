input_file = open('inputd16.txt','r')
input_lines = input_file.readlines()

import re
import copy

def operate(instruction, registers, operator_index):
  reference = {'A': instruction[1], 'B': instruction[2], 'C': instruction[3]}
  if operator_index == 0:
    registers[reference['C']] = registers[reference['A']] + registers[reference['B']]
  elif operator_index == 1:
    registers[reference['C']] = registers[reference['A']] + reference['B']
  elif operator_index == 2:
    registers[reference['C']] = registers[reference['A']] * registers[reference['B']]
  elif operator_index == 3:
    registers[reference['C']] = registers[reference['A']] * reference['B']
  elif operator_index == 4:
    registers[reference['C']] = registers[reference['A']] & registers[reference['B']]
  elif operator_index == 5:
    registers[reference['C']] = registers[reference['A']] & reference['B']
  elif operator_index == 6:
    registers[reference['C']] = registers[reference['A']] | registers[reference['B']]
  elif operator_index == 7:
    registers[reference['C']] = registers[reference['A']] | reference['B']
  elif operator_index == 8:
    registers[reference['C']] = registers[reference['A']]
  elif operator_index == 9:
    registers[reference['C']] = reference['A']
  elif operator_index == 10:
    registers[reference['C']] = 1 if reference['A'] > registers[reference['B']] else 0
  elif operator_index == 11:
    registers[reference['C']] = 1 if registers[reference['A']] > reference['B'] else 0
  elif operator_index == 12:
    registers[reference['C']] = 1 if registers[reference['A']] > registers[reference['B']] else 0
  elif operator_index == 13:
    registers[reference['C']] = 1 if reference['A'] == registers[reference['B']] else 0
  elif operator_index == 14:
    registers[reference['C']] = 1 if registers[reference['A']] == reference['B'] else 0
  elif operator_index == 15:
    registers[reference['C']] = 1 if registers[reference['A']] == registers[reference['B']] else 0
  return registers


line_index = 0
result = 0
possible_operator_indices = [set(range(16)) for i in range(16)]
while input_lines[line_index].startswith('B'):
  registers_before_operation = map(int, re.findall('\d+', input_lines[line_index]))
  instruction = map(int, re.findall('\d+', input_lines[line_index + 1]))
  registers_after_operation = map(int, re.findall('\d+', input_lines[line_index + 2]))

  possible_operator_indices[instruction[0]].intersection_update([opcode if operate(instruction, copy.deepcopy(registers_before_operation), opcode) == registers_after_operation else -1 for opcode in range(16)])
  line_index += 4

operator_indices = [-1] * 16
while operator_indices.count(-1) > 0:
  for opcode in range(16):
    if len(possible_operator_indices[opcode]) == 1:
      operator_indices[opcode] = list(possible_operator_indices[opcode])[0]
  for opcode in range(16):
    possible_operator_indices[opcode].difference_update(operator_indices)

registers = [0] * 4
while line_index < len(input_lines):
  instruction = map(int, re.findall('\d+', input_lines[line_index]))
  if len(instruction) == 4:
    operate(instruction, registers, operator_indices[instruction[0]])
  line_index += 1

print registers[0]
