input_file = open('inputd08.txt','r')
input_lines = input_file.readlines()

character_count_difference = 0
for line in input_lines:
  line = line.strip()
  state = "none"
  character_count_difference += 2
  for char in line:
    if state == "none" and char == '\\':
      state = "backslash"
      continue
    elif state == "backslash":
      if char == '\\' or char == '\"':
        character_count_difference += 1
        state = "none"
        continue
      elif char == 'x':
        state = "nonASCII"
        continue
    elif state == "nonASCII":
      if (char >= '0' and char <= '9') or (char >= 'a' and char <= 'f'):
        state = "nonASCIImiddigit"
        continue
    elif state == "nonASCIImiddigit":
      if (char >= '0' and char <= '9') or (char >= 'a' and char <= 'f'):
        character_count_difference += 3
    state = "none"
print character_count_difference
