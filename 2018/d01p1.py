input_file = open('inputd01.txt','r')
input_lines = input_file.readlines()

freq = 0
for line in input_lines:
  line = int(line.strip())
  freq += line
print freq
