import fileinput

input_lines = list(fileinput.input())

table_size = 5
number_draw_order = map(int, input_lines[0].split(","))
number_of_tables = (len(input_lines) - 1) // (table_size + 1)
tables = [
    [
        list(map(int, input_lines[line_index].strip().replace("  ", " ").split(" ")))
        for line_index in range(
            (table_size + 1) * table_index + 2, (table_size + 1) * (table_index + 1) + 1
        )
    ]
    for table_index in range(number_of_tables)
]


def mask_table(table):
    return [
        [drawn_number in already_drawn_numbers for drawn_number in row] for row in table
    ]


def table_has_bingo(table_drawn_mask):
    return any([all(row) for row in table_drawn_mask]) or any(
        [all(column) for column in zip(*table_drawn_mask)]
    )


def list_tables_with_bingo(table_drawn_masks):
    return [
        table_index
        for table_index, table in enumerate(table_drawn_masks)
        if table_has_bingo(table)
    ]


already_drawn_numbers = []
for number_drawn in number_draw_order:
    already_drawn_numbers.append(number_drawn)
    table_drawn_masks = [mask_table(table) for table in tables]
    tables_with_bingo = list_tables_with_bingo(table_drawn_masks)
    if len(tables_with_bingo) == number_of_tables - 1:
        last_table = list(set(range(number_of_tables)).difference(tables_with_bingo))[0]
    elif len(tables_with_bingo) == number_of_tables:
        print(
            already_drawn_numbers[-1]
            * sum(
                [
                    sum([cell for cell in row if cell not in already_drawn_numbers])
                    for row in tables[last_table]
                ]
            )
        )
        break
