input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

uppercase_lowercase_code_offset = ord('a') - ord('A')
polymer = list(input_lines[0].strip())

unit_index = 0
while unit_index < len(polymer) - 1:
  if abs(ord(polymer[unit_index]) - ord(polymer[unit_index + 1])) == uppercase_lowercase_code_offset:
    del polymer[unit_index : unit_index + 2]
    unit_index = max(unit_index - 1, 0)
  else:
    unit_index += 1

print(len(polymer))
