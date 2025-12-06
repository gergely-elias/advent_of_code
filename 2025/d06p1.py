import fileinput
from math import prod

input_lines = list(fileinput.input())
numbers_in_rows = []
for line in input_lines[:-1]:
    numbers_in_rows.append(list(map(int, line.strip().split())))
operations = input_lines[-1].strip().split()
numbers_in_columns = list(zip(*numbers_in_rows))

OPERATION_TO_FUNCTION = {"+": sum, "*": prod}
print(
    sum(
        OPERATION_TO_FUNCTION[operation](numbers_in_column)
        for operation, numbers_in_column in zip(operations, numbers_in_columns)
    )
)
