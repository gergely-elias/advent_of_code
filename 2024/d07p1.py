import fileinput
import re

input_lines = list(fileinput.input())

calibration_result = 0
for line in input_lines:
    numbers = list(map(int, re.findall(r"\d+", line)))
    test_value = numbers[0]
    possible_expression_values = {numbers[1]}
    for next_element in numbers[2:]:
        updated_expression_values = set()
        for previous_value in possible_expression_values:
            for candidate in [
                previous_value + next_element,
                previous_value * next_element,
            ]:
                if candidate <= test_value:
                    updated_expression_values.add(candidate)
        possible_expression_values = updated_expression_values
    if test_value in possible_expression_values:
        calibration_result += test_value
print(calibration_result)
