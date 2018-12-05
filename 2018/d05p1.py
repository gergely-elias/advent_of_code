input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

uppercase_lowercase_code_offset = ord('a') - ord('A')
polymer = list(input_lines[0].strip())

i = 0
while i < len(polymer) - 1:
  if abs(ord(polymer[i]) - ord(polymer[i + 1])) == uppercase_lowercase_code_offset:
    del polymer[i:i + 2]
    i = max(i - 1, 0)
  else:
    i += 1

print len(polymer)
