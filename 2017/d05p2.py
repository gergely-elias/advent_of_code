input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

message = []
offset = 0
number_of_jumps = 0

for line in input_lines:
  message.append(int(line.strip()))

while offset >= 0 and offset < len(message):
  jump = message[offset]
  if message[offset] >= 3:
    message[offset] -= 1
  else:
    message[offset] += 1
  offset += jump
  number_of_jumps += 1
print number_of_jumps

