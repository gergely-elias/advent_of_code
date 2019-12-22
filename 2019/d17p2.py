input_file = open('inputd17.txt','r')
input_lines = input_file.readlines()

import collections

orig_program = list(map(int, input_lines[0].split(',')))
program = collections.defaultdict(lambda: 0)
for memory_index, code in enumerate(orig_program):
  program[memory_index] = code
program[0] = 2

operation_scheme = {
  1: 'rrw',
  2: 'rrw',
  3: 'w',
  4: 'r',
  5: 'rr',
  6: 'rr',
  7: 'rrw',
  8: 'rrw',
  9: 'r',
  99: ''
}

number_of_parameters = {op: len(operation_scheme[op]) for op in operation_scheme}
addressable_length = {op: operation_scheme[op].count('r') for op in operation_scheme}
write_parameter_index = {op: operation_scheme[op].index('w') if 'w' in operation_scheme[op] else None for op in operation_scheme}
inp_index = 0
position = 0
relative_base = 0
complete_output = ''
robot_directions = ['^', '>', 'v', '<']
direction_steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def compress(commands_complete_list, compressed_version, compression_position, compression_mappings):
  global inputs_to_encode, inputs
  if len(compression_mappings) > 0:
    while any([commands_complete_list[compression_position : compression_position + len(mapping)] == mapping for mapping in compression_mappings]):
      matched_mapping_index = [commands_complete_list[compression_position : compression_position + len(mapping)] == mapping for mapping in compression_mappings].index(True)
      compression_position += len(compression_mappings[matched_mapping_index])
      compressed_version.append(matched_mapping_index)
  
  if compression_position == len(commands_complete_list):
    if len(compression_mappings) <= 3 and all([len(','.join(mapping)) <= 20 for mapping in compression_mappings]):
      inputs_to_encode = [','.join(['ABC'[i] for i in compressed_version]) + '\n'] + [','.join(mapping)+'\n' for mapping in compression_mappings] + ['n\n']
      inputs = [ord(character) for character in ''.join(inputs_to_encode)]
  if len(compression_mappings) > 3 or any([len(','.join(mapping)) > 20 for mapping in compression_mappings]):
    return
  
  for next_length in range(1, len(commands_complete_list) - compression_position):
    compress(commands_complete_list, compressed_version + [len(compression_mappings)], compression_position + next_length, compression_mappings + [commands_complete_list[compression_position : compression_position + next_length]])

while position < len(program):
  operation_with_mode_indicators = program[position]
  operation = operation_with_mode_indicators % 100
  mode_indicators = [(operation_with_mode_indicators // (10 ** decimal_place)) % 10 for decimal_place in [2, 3, 4]]
  opcode_parameters = [program[character] for character in range(position + 1, position + number_of_parameters[operation] + 1)]
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
    if inp_index == 0:
      camera_output = [row.strip() for row in complete_output.split('\n')[:-3]]
      scaffold = collections.defaultdict(lambda: '.')
      sy = len(camera_output)
      sx = len(camera_output[0])
      robot_position = None
      robot_direction = None
      for y in range(sy):
        for x in range(sx):
          if camera_output[y][x] == '#':
            scaffold[(y, x)] = '#'
          if camera_output[y][x] in robot_directions:
            robot_position = (y, x)
            robot_direction = robot_directions.index(camera_output[y][x])

      reached_end = False
      command_list = []
      while not reached_end:
        step_counter = 0
        while scaffold[tuple([current + step for (current, step) in zip(robot_position, direction_steps[robot_direction])])] == '#':
          step_counter += 1
          robot_position = tuple([current + step for (current, step) in zip(robot_position, direction_steps[robot_direction])])
        if step_counter > 0:
          command_list.append(str(step_counter))
        if scaffold[tuple([current + step for (current, step) in zip(robot_position, direction_steps[(robot_direction + 1) % 4])])] == '#':
          robot_direction = (robot_direction + 1) % 4
          command_list.append('R')
        elif scaffold[tuple([current + step for (current, step) in zip(robot_position, direction_steps[(robot_direction - 1) % 4])])] == '#':
          robot_direction = (robot_direction - 1) % 4
          command_list.append('L')
        else:
          reached_end = True

      total_length = len(command_list)
      main_function = []
      compression_position = 0
      compress(command_list, main_function, compression_position, [])

    input_parameter = inputs[inp_index]
    program[write_parameter_address] = input_parameter
    inp_index += 1
  elif operation == 4:
    output_parameter = address[0]
    if output_parameter in range(256):
      complete_output += chr(output_parameter)
    else:
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
