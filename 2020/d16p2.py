import fileinput
import networkx
import re
import math

input_lines = list(fileinput.input())

ticket_field_rules, my_ticket, nearby_tickets = "".join(input_lines).split("\n\n")

ranges_of_fields = {
    line[: line.index(":")]: list(
        map(
            lambda range: list(map(int, range.split("-"))), re.findall(r"\d+-\d+", line)
        )
    )
    for line in ticket_field_rules.strip().split("\n")
}

my_ticket = list(map(int, my_ticket.strip().split("\n")[1].split(",")))

tickets = [
    list(map(int, line.split(","))) for line in nearby_tickets.strip().split("\n")[1:]
]

max_valid_number = max(
    [
        ranges_of_single_field[-1][-1]
        for ranges_of_single_field in ranges_of_fields.values()
    ]
)

number_can_be_valid = [False] * (max_valid_number + 1)
for ranges_of_single_field in ranges_of_fields.values():
    for range_start, range_finish in ranges_of_single_field:
        number_can_be_valid[range_start : range_finish + 1] = [True] * (
            range_finish - range_start + 1
        )

valid_tickets = [
    t
    for t in tickets
    if all([tf <= max_valid_number and number_can_be_valid[tf] for tf in t])
]

valid_numbers_of_field = dict()
for field_name, ranges_of_single_field in ranges_of_fields.items():
    number_can_be_valid_in_field = [False] * (max_valid_number + 1)
    for range_start, range_finish in ranges_of_single_field:
        number_can_be_valid_in_field[range_start : range_finish + 1] = [True] * (
            range_finish - range_start + 1
        )
    valid_numbers_of_field[field_name] = number_can_be_valid_in_field

field_column = networkx.Graph()
field_node_prefix = "f_"
column_node_prefix = "c_"
for field, valid_numbers in valid_numbers_of_field.items():
    for column in range(len(my_ticket)):
        if all([valid_numbers[ticket[column]] for ticket in valid_tickets]):
            field_column.add_edge(
                field_node_prefix + field, column_node_prefix + str(column)
            )

pairing = networkx.bipartite.maximum_matching(field_column)
print(
    math.prod(
        [
            my_ticket[int(column[2:])]
            for field, column in pairing.items()
            if field.startswith(field_node_prefix + "departure")
        ]
    )
)
