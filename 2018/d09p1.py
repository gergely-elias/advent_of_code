input_file = open('inputd09.txt','r')
input_lines = input_file.readlines()

import re

players, marbles = map(int, re.findall('\d+', input_lines[0].strip()))

prev_marble = [0]
next_marble = [0]
scores = players * [0]
marble_in_position = 0

for marble_on_turn in range(1, marbles + 1):
  if marble_on_turn % 23 == 0:
    for back_steps in range(7):
      marble_in_position = prev_marble[marble_in_position]
    scores[(marble_on_turn - 1) % players] += marble_on_turn + next_marble[marble_in_position]

    marble_to_remove = next_marble[marble_in_position]
    prev_marble[next_marble[marble_to_remove]] = prev_marble[marble_to_remove]
    next_marble[prev_marble[marble_to_remove]] = next_marble[marble_to_remove]
    prev_marble[marble_to_remove] = -1
    next_marble[marble_to_remove] = -1

  else:
    for steps in range(2):
      marble_in_position = next_marble[marble_in_position]
    while marble_on_turn >= len(next_marble):
      prev_marble.append(-1)
      next_marble.append(-1)
    
    marble_to_insert = marble_on_turn
    prev_marble[marble_to_insert] = marble_in_position
    next_marble[marble_to_insert] = next_marble[marble_in_position]
    prev_marble[next_marble[marble_in_position]] = marble_to_insert
    next_marble[marble_in_position] = marble_to_insert

print(max(scores))
