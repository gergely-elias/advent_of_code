import fileinput

input_lines = list(fileinput.input())

number_of_ups = 0
number_of_downs = 0
for character in input_lines[0]:
    if character == "(":
        number_of_ups += 1
    elif character == ")":
        number_of_downs += 1
    if number_of_downs > number_of_ups:
        print(number_of_ups + number_of_downs)
        exit()
