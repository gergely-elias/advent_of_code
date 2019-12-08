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
for phase_setting_sequence in itertools.permutations(range(5,10)):
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
        if first_input[amp_index]:
          input_parameter = phase_setting_sequence[amp_index]
          first_input[amp_index] = False
        else:
          input_parameter = signal_to_transmit
        program[last_parameter] = input_parameter
      elif operation == 4:
        output_parameter = address[0]
        if output_parameter != 0:
          signal_to_transmit = output_parameter
          position += opcode_length[operation]
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
        program[last_parameter] = 1 if address[0] < address[1] else 0
      elif operation == 8:
        program[last_parameter] = 1 if address[0] == address[1] else 0
      else:
        program_halted = True
        break
      position += opcode_length[operation]
      positions[amp_index] = position
    if program_halted:
      break
  if (signal_to_transmit > max_thruster_signal):
    max_thruster_signal = signal_to_transmit
print(max_thruster_signal)
