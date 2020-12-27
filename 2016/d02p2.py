import fileinput

input_lines = list(fileinput.input())

position = [0, -2]
code = ""
mapping = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]

for line in input_lines:
    for move in line:
        save_position = position[:]
        if move == "U":
            position[0] -= 1
        elif move == "D":
            position[0] += 1
        elif move == "R":
            position[1] += 1
        elif move == "L":
            position[1] -= 1
        if sum(abs(i) for i in position) > 2:
            position = save_position[:]
    code += mapping[position[0] + 2][position[1] + 2]

print(code)
