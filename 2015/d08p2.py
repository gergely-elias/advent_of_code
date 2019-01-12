input_file = open('inputd08.txt','r')
input_lines = input_file.readlines()

character_count_difference = 0
for line in input_lines:
  line = line.strip()
  character_count_difference += 2
  for char in line:
    if char == '\\' or char == '\"':
      character_count_difference += 1
print(character_count_difference)
