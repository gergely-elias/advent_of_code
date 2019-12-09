input_file = open('inputd07.txt','r')
input_lines = input_file.readlines()

import itertools

orig_program = list(map(int, input_lines[0].split(',')))

number_of_parameters = {}
for operation in [99]:
  number_of_parameters[operation] = 0
for operation in [3, 4]:
  number_of_parameters[operation] = 1
for operation in [5, 6]:
  number_of_parameters[operation] = 2
for operation in [1, 2, 7, 8]:
  number_of_parameters[operation] = 3 

addressable_length = {}
for operation in [3, 99]:
  addressable_length[operation] = 0
for operation in [4]:
  addressable_length[operation] = 1
for operation in [1, 2, 5, 6, 7, 8]:
  addressable_length[operation] = 2

write_parameter_index = {}
for operation in [4, 5, 6, 99]:
  write_parameter_index[operation] = None
for operation in [3]:
  write_parameter_index[operation] = 0
for operation in [1, 2, 7, 8]:
  write_parameter_index[operation] = 2

max_thruster_signal = -float("inf")
for phase_setting_sequence in itertools.permutations(range(5)):
  signal_to_transmit = 0
  first_input = True
  for phase_setting in phase_setting_sequence:
    program = orig_program[:]
    position = 0
    while position < len(program):
      operation_with_mode_indicators = program[position]
      operation = operation_with_mode_indicators % 100
      mode_indicators = [(operation_with_mode_indicators // (10 ** decimal_place)) % 10 for decimal_place in [2, 3, 4]]
      opcode_parameters = program[position + 1 : position + number_of_parameters[operation] + 1]
      address = [program[opcode_parameters[index]] if mode_indicators[index] == 0 else opcode_parameters[index] for index in range(addressable_length[operation])]
      write_parameter_address = None if write_parameter_index[operation] is None else \
        opcode_parameters[write_parameter_index[operation]]

      if operation == 1:
        program[write_parameter_address] = address[0] + address[1]
      elif operation == 2:
        program[write_parameter_address] = address[0] * address[1]
      elif operation == 3:
        if first_input:
          input_parameter = phase_setting
        else:
          input_parameter = signal_to_transmit
        first_input = not first_input
        program[write_parameter_address] = input_parameter
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
        program[write_parameter_address] = 1 if address[0] < address[1] else 0
      elif operation == 8:
        program[write_parameter_address] = 1 if address[0] == address[1] else 0
      else:
        assert(operation == 99)
        break
      position += number_of_parameters[operation] + 1
  if (signal_to_transmit > max_thruster_signal):
    max_thruster_signal = signal_to_transmit
print(max_thruster_signal)
