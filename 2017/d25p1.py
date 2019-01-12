input_file = open('inputd25.txt','r')
input_lines = input_file.readlines()

import re

position = 0
state_machine = {}

state = re.findall('(?<=state )[A-Z]+(?=\.)', input_lines[0])[0]
steps = int(re.findall('\d+', input_lines[1])[0])
line_index = 3
while line_index < len(input_lines):
  described_state = re.findall('(?<=state )[A-Z]+(?=:)', input_lines[line_index])[0]
  line_index += 1
  state_descriptions = [[] for value_index in range(2)]
  for value_index in range(2):
    described_value = int(re.findall('\d+', input_lines[line_index])[0])
    line_index += 1
    state_descriptions[described_value].append(int(re.findall('\d+', input_lines[line_index])[0])) 
    line_index += 1
    state_descriptions[described_value].append(1 if re.findall('(?<=to the )\w+(?=\.)', input_lines[line_index])[0] == 'right' else -1 ) 
    line_index += 1
    state_descriptions[described_value].append(re.findall('(?<=state )[A-Z]+(?=\.)', input_lines[line_index])[0]) 
    line_index += 1
  state_machine[described_state] = state_descriptions
  line_index += 1

import collections
tape = collections.defaultdict(lambda: 0)

for step in range(steps):
  value = state_machine[state][tape[position]]
  tape[position] = value[0]
  position += value[1]
  state = value[2]
  
checksum = 0
for reg in tape:
  checksum += tape[reg]
print(checksum)

