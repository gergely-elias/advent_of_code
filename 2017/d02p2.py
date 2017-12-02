input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

checksum = 0
for line in input_lines:
  numbers_on_line = [int(x) for x in line.strip().split('\t')]
  line_length = len(numbers_on_line)
  numbers_on_line_found = False
  for i in range(line_length):
    for j in range(line_length):
      if i != j and numbers_on_line[i] % numbers_on_line[j] == 0:
        checksum += numbers_on_line[i]/numbers_on_line[j]
        numbers_on_line_found = True
        break
    if numbers_on_line_found:
      break
print checksum
