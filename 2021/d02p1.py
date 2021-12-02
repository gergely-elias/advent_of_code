import fileinput

input_lines = list(fileinput.input())

x = 0
y = 0
for line in input_lines:
    command, value = line.split()
    value = int(value)
    if command == "forward":
        x += value
    elif command == "up":
        y -= value
    elif command == "down":
        y += value
print(x * y)
