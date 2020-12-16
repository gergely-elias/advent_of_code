import fileinput
import re

input_lines = list(fileinput.input())

ticket_field_rules, my_ticket, nearby_tickets = "".join(input_lines).split("\n\n")

ranges_of_fields = [
    list(
        map(lambda range: list(map(int, range.split("-"))), re.findall("\d+-\d+", line))
    )
    for line in ticket_field_rules.strip().split("\n")
]

tickets = [
    list(map(int, line.split(","))) for line in nearby_tickets.strip().split("\n")[1:]
]

max_valid_number = max(
    [ranges_of_single_field[-1][-1] for ranges_of_single_field in ranges_of_fields]
)
number_can_be_valid = [False] * (max_valid_number + 1)

for ranges_of_single_field in ranges_of_fields:
    for range_start, range_finish in ranges_of_single_field:
        number_can_be_valid[range_start : range_finish + 1] = [True] * (
            range_finish - range_start + 1
        )

print(
    sum(
        [
            sum(
                [
                    ticket_field
                    for ticket_field in ticket
                    if ticket_field > max_valid_number
                    or not number_can_be_valid[ticket_field]
                ]
            )
            for ticket in tickets
        ]
    )
)
