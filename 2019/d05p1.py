input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

program = list(map(int, input_lines[0].split(',')))

opcode_length = {}
for operation in [3, 4]:
  opcode_length[operation] = 2
for operation in [1, 2, 99]:
  opcode_length[operation] = 4 

addressable_length = {}
for operation in [3, 99]:
  addressable_length[operation] = 0
for operation in [4]:
  addressable_length[operation] = 1
for operation in [1, 2]:
  addressable_length[operation] = 2

position = 0
while position < len(program):
  operation_with_mode_bits = program[position]
  operation = operation_with_mode_bits % 100
  mode_indicators = [(operation_with_mode_bits // (10 ** decimal_place)) % 10 for decimal_place in [2,3,4]]
  opcode_parameters = program[position + 1 : position + opcode_length[operation]]
  address = [program[opcode_parameters[index]] if mode_indicators[index] == 0 else opcode_parameters[index] for index in range(addressable_length[operation])]
  last_parameter = opcode_parameters[-1]

  if operation == 1:
    program[last_parameter] = address[0] + address[1]
  elif operation == 2:
    program[last_parameter] = address[0] * address[1]
  elif operation == 3:
    input_parameter = 1
    program[last_parameter] = input_parameter
  elif operation == 4:
    output_parameter = address[0]
    if output_parameter != 0:
      print(output_parameter)
      exit()
  else:
    break
  position += opcode_length[operation]
