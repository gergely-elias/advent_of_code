import fileinput

input_lines = list(fileinput.input())

print(sum([int(line.strip()) for line in input_lines]))
