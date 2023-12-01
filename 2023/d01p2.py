import fileinput
from string import digits

input_lines = list(line.strip() for line in fileinput.input())
spelt_digits = {
    digit: spelt_digit
    for digit, spelt_digit in zip(
        range(1, 10),
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
    )
}

calibration_value = 0
for line in input_lines:
    first_found_digit, last_found_digit = None, None
    for char_index in range(len(line)):
        if line[char_index] in digits:
            first_found_digit = int(line[char_index])
            break
        for digit, spelt_digit in spelt_digits.items():
            if line[char_index:].startswith(spelt_digit):
                first_found_digit = digit
                break
        if first_found_digit is not None:
            break
    for char_index in range(len(line) - 1, -1, -1):
        if line[char_index] in digits:
            last_found_digit = int(line[char_index])
            break
        for digit, spelt_digit in spelt_digits.items():
            if line[: char_index + 1].endswith(spelt_digit):
                last_found_digit = digit
                break
        if last_found_digit is not None:
            break
    calibration_value += 10 * first_found_digit + last_found_digit
print(calibration_value)
