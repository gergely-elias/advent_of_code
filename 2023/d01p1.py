import fileinput
from string import digits

input_lines = list(line.strip() for line in fileinput.input())

calibration_value = 0
for line in input_lines:
    digits_on_line = [int(d) for d in line if d in digits]
    calibration_value += 10 * digits_on_line[0] + digits_on_line[-1]
print(calibration_value)
