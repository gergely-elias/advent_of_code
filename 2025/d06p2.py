import fileinput
from math import prod

input_lines = list(fileinput.input())
digits_in_rows = []
for line in input_lines[:-1]:
    digits_in_rows.append(line.strip("\n"))
digits_in_columns = list(zip(*digits_in_rows))

line_of_operations = input_lines[-1].strip("\n")
operation_start_column_indices = [
    i for i, c in enumerate(line_of_operations) if c != " "
] + [len(line_of_operations) + 1]
operations = input_lines[-1].strip().split()

OPERATION_TO_FUNCTION = {"+": sum, "*": prod}
print(
    sum(
        OPERATION_TO_FUNCTION[operation](
            int("".join(digits_in_columns[column_index]).strip())
            for column_index in range(start_column, next_start_column - 1)
        )
        for operation, start_column, next_start_column in zip(
            operations,
            operation_start_column_indices[:-1],
            operation_start_column_indices[1:],
        )
    )
)
