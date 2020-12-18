import fileinput
import re

input_lines = list(fileinput.input())


def expression_value(expression_match):
    parsed_expression = expression_match.group()[1:-1].split()
    value = int(parsed_expression[0])
    for term_index in range(1, len(parsed_expression), 2):
        if parsed_expression[term_index] == "+":
            value += int(parsed_expression[term_index + 1])
        elif parsed_expression[term_index] == "*":
            value *= int(parsed_expression[term_index + 1])
        else:
            assert False
    return str(value)


sum_of_lines = 0
for line in input_lines:
    reduced_line = "(" + line.strip() + ")"
    while "(" in reduced_line:
        reduced_line = re.sub("\([^\(\)]+\)", expression_value, reduced_line)
    sum_of_lines += int(reduced_line)
print(sum_of_lines)
