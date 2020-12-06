import fileinput

input_lines = list(fileinput.input())

message = []
offset = 0
number_of_jumps = 0

for line in input_lines:
    message.append(int(line.strip()))

while offset >= 0 and offset < len(message):
    jump = message[offset]
    message[offset] += 1
    offset += jump
    number_of_jumps += 1
print(number_of_jumps)
