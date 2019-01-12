input_file = open('inputd18.txt','r')
input_lines = input_file.readlines()

import re
import collections

instructions = [line.strip().split() for line in input_lines]
program_state = []
for program_id in range(2):
  program_state.append({})
  program_state[program_id]['registers'] = collections.defaultdict(lambda: 0)
  program_state[program_id]['registers']['p'] = program_id
  program_state[program_id]['instruction_index'] = 0
  program_state[program_id]['receive_queue'] = []
  program_state[program_id]['waiting_for_receive'] = False
count_of_messages = 0
program_id = 0

def substitute(program_id, value):
  if re.match('-?\d+', value):
    return int(value)
  return program_state[program_id]['registers'][value]


while not (program_state[0]['waiting_for_receive'] and program_state[1]['waiting_for_receive']):
  while program_state[program_id]['instruction_index'] in range(0, len(instructions)) and not program_state[program_id]['waiting_for_receive']:
    instruction = instructions[program_state[program_id]['instruction_index']]
    if instruction[0] == 'set':
      program_state[program_id]['registers'][instruction[1]] = substitute(program_id, instruction[2])
    elif instruction[0] == 'add':
      program_state[program_id]['registers'][instruction[1]] += substitute(program_id, instruction[2])
    elif instruction[0] == 'mul':
      program_state[program_id]['registers'][instruction[1]] *= substitute(program_id, instruction[2])
    elif instruction[0] == 'mod':
      program_state[program_id]['registers'][instruction[1]] %= substitute(program_id, instruction[2])
    elif instruction[0] == 'jgz' and substitute(program_id, instruction[1])>0:
      program_state[program_id]['instruction_index'] += substitute(program_id, instruction[2])
      continue
    elif instruction[0] == 'rcv':
      if len(program_state[program_id]['receive_queue']) > 0:
        program_state[program_id]['registers'][instruction[1]] = program_state[program_id]['receive_queue'].pop(0)
      else:
        program_state[program_id]['waiting_for_receive'] = True
        break
    elif instruction[0] == 'snd':
      program_state[1 - program_id]['receive_queue'].append(substitute(program_id, instruction[1]))
      program_state[1 - program_id]['waiting_for_receive'] = False
      if program_id == 1:
        count_of_messages += 1
    program_state[program_id]['instruction_index'] += 1
  program_id = 1 - program_id

print(count_of_messages)
