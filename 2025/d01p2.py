import fileinput

input_lines = list(fileinput.input())

DIAL_SIZE = 100
dial_position = 50
count = 0
for line in input_lines:
    prev_dial_position = dial_position
    instruction, amount = line[0], int(line[1:])
    if instruction == "L":
        amount *= -1
    dial_position += amount
    if (dial_position < 0 and prev_dial_position % DIAL_SIZE) or (
        dial_position > DIAL_SIZE and dial_position % DIAL_SIZE
    ):
        count += abs(dial_position // DIAL_SIZE - prev_dial_position // DIAL_SIZE)
    elif dial_position < 0 or dial_position > DIAL_SIZE:
        count += abs(dial_position // DIAL_SIZE - prev_dial_position // DIAL_SIZE) - 1
    dial_position %= DIAL_SIZE
    if dial_position == 0:
        count += 1
print(count)
