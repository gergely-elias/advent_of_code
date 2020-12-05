input_file = open("inputd01.txt", "r")
input_lines = input_file.readlines()

print(sum([int(line.strip()) for line in input_lines]))
