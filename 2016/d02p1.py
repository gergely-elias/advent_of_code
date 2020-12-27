import fileinput

input_lines = list(fileinput.input())

position = 5
code = ""

for line in input_lines:
    for move in line:
        if move == "U" and position > 3:
            position -= 3
        elif move == "D" and position < 7:
            position += 3
        elif move == "R" and position % 3 != 0:
            position += 1
        elif move == "L" and position % 3 != 1:
            position -= 1
    code += str(position)

print(code)
