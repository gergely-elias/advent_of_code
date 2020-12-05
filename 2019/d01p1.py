input_file = open("inputd01.txt", "r")
input_lines = input_file.readlines()

print(sum([int(line.strip()) // 3 - 2 for line in input_lines]))
