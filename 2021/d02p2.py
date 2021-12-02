import fileinput

input_lines = list(fileinput.input())

x = 0
y = 0
aim = 0
for line in input_lines:
    command, value = line.split()
    value = int(value)
    if command == "forward":
        x += value
        y += aim * value
    if command == "up":
        aim -= value
    if command == "down":
        aim += value
print(x * y)
