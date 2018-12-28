input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

import itertools

for (line_1, line_2) in itertools.combinations([line.strip() for line in input_lines], 2):
  different_letters = 0
  for letter_index in range(len(line_1)):
    if line_1[letter_index] != line_2[letter_index]:
      different_letters += 1
      difference_position = letter_index
    if different_letters > 1:
      break
  if different_letters == 1:
    print(line_1[:difference_position] + line_1[difference_position + 1:])
    break
