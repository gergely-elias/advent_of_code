input_file = open("inputd02.txt", "r")
input_lines = input_file.readlines()

checksum = 0
for line in input_lines:
    numbers_on_line = [int(x) for x in line.strip().split("\t")]
    line_length = len(numbers_on_line)
    numbers_on_line_found = False
    for i1, x1 in enumerate(numbers_on_line):
        for i2, x2 in enumerate(numbers_on_line):
            if i1 != i2 and x1 % x2 == 0:
                checksum += x1 // x2
                numbers_on_line_found = True
                break
        if numbers_on_line_found:
            break
print(checksum)
