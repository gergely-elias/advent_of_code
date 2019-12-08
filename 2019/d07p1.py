input_file = open('inputd07.txt','r')
input_lines = input_file.readlines()

import itertools

orig_program = list(map(int, input_lines[0].split(',')))

opcode_length = {}
for operation in [99]:
  opcode_length[operation] = 1
for operation in [3, 4]:
  opcode_length[operation] = 2
for operation in [5, 6]:
  opcode_length[operation] = 3
for operation in [1, 2, 7, 8]:
  opcode_length[operation] = 4 

addressable_length = {}
for operation in [3, 99]:
  addressable_length[operation] = 0
for operation in [4]:
  addressable_length[operation] = 1
for operation in [1, 2, 5, 6, 7, 8]:
  addressable_length[operation] = 2

max_thruster_signal = -float("inf")
for phase_setting_sequence in itertools.permutations(range(5)):
  signal_to_transmit = 0
  first_input = True
  for phase_setting in phase_setting_sequence:
    program = orig_program[:]
    position = 0
    while position < len(program):
      operation_with_mode_bits = program[position]
      operation = operation_with_mode_bits % 100
      mode_indicators = [(operation_with_mode_bits // (10 ** decimal_place)) % 10 for decimal_place in [2,3,4]]
      opcode_parameters = program[position + 1 : position + opcode_length[operation]]
      address = [program[opcode_parameters[index]] if mode_indicators[index] == 0 else opcode_parameters[index] for index in range(addressable_length[operation])]
      last_parameter = opcode_parameters[-1] if len(opcode_parameters) > 0 else None

      if operation == 1:
        program[last_parameter] = address[0] + address[1]
      elif operation == 2:
        program[last_parameter] = address[0] * address[1]
      elif operation == 3:
        if first_input:
          input_parameter = phase_setting
        else:
          input_parameter = signal_to_transmit
        first_input = not first_input
        program[last_parameter] = input_parameter
      elif operation == 4:
        output_parameter = address[0]
        if output_parameter != 0:
          signal_to_transmit = output_parameter
      elif operation == 5:
        if address[0] != 0:
          position = address[1]
          continue
      elif operation == 6:
        if address[0] == 0:
          position = address[1]
          continue
      elif operation == 7:
        program[last_parameter] = 1 if address[0] < address[1] else 0
      elif operation == 8:
        program[last_parameter] = 1 if address[0] == address[1] else 0
      else:
        break
      position += opcode_length[operation]
  if (signal_to_transmit > max_thruster_signal):
    max_thruster_signal = signal_to_transmit
print(max_thruster_signal)
