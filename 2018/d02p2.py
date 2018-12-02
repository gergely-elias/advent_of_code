input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

input_lines = [line.strip() for line in input_lines]

import itertools
for (line_1, line_2) in itertools.combinations(input_lines, 2):
  different_letters = 0
  for i in range(len(line_1)):
    if line_1[i] != line_2[i]:
      different_letters += 1
      difference_position = i
    if different_letters > 1:
      break
  if different_letters == 1:
    print line_1[:difference_position] + line_1[difference_position + 1:]
    exit()
