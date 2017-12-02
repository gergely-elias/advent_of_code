input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

checksum = 0
for line in input_lines:
  numbers_on_line = [int(x) for x in line.strip().split('\t')]
  checksum += max(numbers_on_line) - min(numbers_on_line)
print checksum
