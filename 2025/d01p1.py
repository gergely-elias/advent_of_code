import fileinput

input_lines = list(fileinput.input())

DIAL_SIZE = 100
dial_position = 50
count = 0
for line in input_lines:
    instruction, amount = line[0], int(line[1:])
    if instruction == "L":
        amount *= -1
    dial_position += amount
    dial_position %= DIAL_SIZE
    if dial_position == 0:
        count += 1
print(count)
