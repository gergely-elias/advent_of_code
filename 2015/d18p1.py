import fileinput

input_lines = list(fileinput.input())

table_size = len(input_lines)
table = (table_size + 2) * [[]]
for row_index in range(table_size + 2):
    table[row_index] = (table_size + 2) * [0]
for (row_index, line) in enumerate(input_lines):
    line = line.strip()
    for (column_index, char) in enumerate(line):
        if char == "#":
            table[row_index + 1][column_index + 1] = 1

neighbour_diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
next_table = (table_size + 2) * [[]]
for row_index in range(table_size + 2):
    next_table[row_index] = (table_size + 2) * [0]

total_steps = 100
for steps in range(total_steps):
    for row_index in range(1, table_size + 1):
        for column_index in range(1, table_size + 1):
            neighbours = 0
            for neighbour_diff in neighbour_diffs:
                neighbours += table[row_index + neighbour_diff[0]][
                    column_index + neighbour_diff[1]
                ]
            next_table[row_index][column_index] = table[row_index][column_index]
            if neighbours == 3:
                next_table[row_index][column_index] = 1
            elif neighbours != 2:
                next_table[row_index][column_index] = 0

    for row_index in range(1, table_size + 1):
        for column_index in range(1, table_size + 1):
            table[row_index][column_index] = next_table[row_index][column_index]
print(sum(map(sum, table)))
