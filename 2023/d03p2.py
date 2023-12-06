import collections
import fileinput
import math
import string

input_lines = [line.strip() for line in fileinput.input()]

gear_positions = []
numbers_by_positions = {}
for y in range(len(input_lines)):
    for x in range(len(input_lines[y])):
        if input_lines[y][x] in string.digits and (
            x == 0 or input_lines[y][x - 1] not in string.digits
        ):
            digit_index = 0
            number_value = 0
            while (
                x + digit_index < len(input_lines[y])
                and input_lines[y][x + digit_index] in string.digits
            ):
                number_value = 10 * number_value + int(input_lines[y][x + digit_index])
                digit_index += 1
            numbers_by_positions[(y, x, x + digit_index - 1)] = number_value
        if input_lines[y][x] == "*":
            gear_positions.append((y, x))

numbers_by_gear_coords = collections.defaultdict(list)
for (y, x_start, x_end), number_value in numbers_by_positions.items():
    min_neighbour_y = max(y - 1, 0)
    max_neighbour_y = min(y + 1, len(input_lines) - 1)
    min_neighbour_x = max(x_start - 1, 0)
    max_neighbour_x = min(x_end + 1, len(input_lines[0]) - 1)
    for x in range(min_neighbour_x, max_neighbour_x + 1):
        for y in range(min_neighbour_y, max_neighbour_y + 1):
            if (y, x) in gear_positions:
                numbers_by_gear_coords[(y, x)].append(number_value)

sum_of_gear_ratios = 0
for gear_numbers in numbers_by_gear_coords.values():
    if len(gear_numbers) == 2:
        sum_of_gear_ratios += math.prod(gear_numbers)
print(sum_of_gear_ratios)
