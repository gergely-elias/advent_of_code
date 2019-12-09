input_file = open('inputd09.txt','r')
input_lines = input_file.readlines()

import collections

orig_program = list(map(int, input_lines[0].split(',')))
program = collections.defaultdict(lambda: 0)
for memory_index, code in enumerate(orig_program):
  program[memory_index] = code

number_of_parameters = {}
for operation in [99]:
  number_of_parameters[operation] = 0
for operation in [3, 4, 9]:
  number_of_parameters[operation] = 1
for operation in [5, 6]:
  number_of_parameters[operation] = 2
for operation in [1, 2, 7, 8]:
  number_of_parameters[operation] = 3 

addressable_length = {}
for operation in [3, 99]:
  addressable_length[operation] = 0
for operation in [4, 9]:
  addressable_length[operation] = 1
for operation in [1, 2, 5, 6, 7, 8]:
  addressable_length[operation] = 2

write_parameter_index = {}
for operation in [4, 5, 6, 9, 99]:
  write_parameter_index[operation] = None
for operation in [3]:
  write_parameter_index[operation] = 0
for operation in [1, 2, 7, 8]:
  write_parameter_index[operation] = 2

position = 0
relative_base = 0
while position < len(program):
  operation_with_mode_indicators = program[position]
  operation = operation_with_mode_indicators % 100
  mode_indicators = [(operation_with_mode_indicators // (10 ** decimal_place)) % 10 for decimal_place in [2, 3, 4]]
  opcode_parameters = [program[x] for x in range(position + 1, position + number_of_parameters[operation] + 1)]
  address = {}
  for index in range(addressable_length[operation]):
    if mode_indicators[index] == 1:
      address[index] = opcode_parameters[index]
    else:
      assert(mode_indicators[index] in [0, 2])
      address[index] = program[opcode_parameters[index] + (relative_base if mode_indicators[index] == 2 else 0)]
  write_parameter_address = None if write_parameter_index[operation] is None else \
    opcode_parameters[write_parameter_index[operation]] + \
    (relative_base if mode_indicators[write_parameter_index[operation]] == 2 else 0)

  if operation == 1:
    program[write_parameter_address] = address[0] + address[1]
  elif operation == 2:
    program[write_parameter_address] = address[0] * address[1]
  elif operation == 3:
    input_parameter = 2
    program[write_parameter_address] = input_parameter
  elif operation == 4:
    output_parameter = address[0]
    if output_parameter != 0:
      print(output_parameter)
  elif operation == 5:
    if address[0] != 0:
      position = address[1]
      continue
  elif operation == 6:
    if address[0] == 0:
      position = address[1]
      continue
  elif operation == 7:
    program[write_parameter_address] = 1 if address[0] < address[1] else 0
  elif operation == 8:
    program[write_parameter_address] = 1 if address[0] == address[1] else 0
  elif operation == 9:
    relative_base += address[0]
  else:
    assert(operation == 99)
    break
  position += number_of_parameters[operation] + 1
