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
for phase_setting_sequence in itertools.permutations(range(5, 10)):
  amp_index = 0
  signal_to_transmit = 0
  first_input = [True] * 5
  program_halted = False
  programs = [orig_program[:]] * 5
  positions = [0] * 5
  final_output = 0
  while True:
    program = programs[amp_index]
    position = positions[amp_index]
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
        if first_input[amp_index]:
          input_parameter = phase_setting_sequence[amp_index]
          first_input[amp_index] = False
        else:
          input_parameter = signal_to_transmit
        program[write_parameter_address] = input_parameter
      elif operation == 4:
        output_parameter = address[0]
        if output_parameter != 0:
          signal_to_transmit = output_parameter
          position += number_of_parameters[operation] + 1
          positions[amp_index] = position
          amp_index = (amp_index + 1) % 5
          break
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
        assert(operation == 99 and amp_index == 0)
        program_halted = True
        break
      position += number_of_parameters[operation] + 1
      positions[amp_index] = position
    if program_halted:
      break
  if (signal_to_transmit > max_thruster_signal):
    max_thruster_signal = signal_to_transmit
print(max_thruster_signal)
