import fileinput

input_lines = list(fileinput.input())

print(sum([int(line.strip()) // 3 - 2 for line in input_lines]))
