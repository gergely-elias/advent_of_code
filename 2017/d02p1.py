import fileinput

input_lines = list(fileinput.input())

checksum = 0
for line in input_lines:
    numbers_on_line = [int(x) for x in line.strip().split("\t")]
    checksum += max(numbers_on_line) - min(numbers_on_line)
print(checksum)
