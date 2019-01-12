input_file = open('inputd06.txt','r')
input_lines = input_file.readlines()

line = input_lines[0].strip().split('\t')
blocks = [int(x) for x in line]
states_already_seen = {}
state_counter = 0

while tuple(blocks) not in states_already_seen:
  states_already_seen[tuple(blocks)] = state_counter
  state_counter += 1
  maximal_value = max(blocks)
  maximal_position = blocks.index(maximal_value)

  blocks[maximal_position] = 0
  for j in range(maximal_value):
    blocks[(maximal_position + 1 + j) % len(blocks)] += 1

print(state_counter - states_already_seen[tuple(blocks)])
