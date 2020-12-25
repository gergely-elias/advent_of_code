import fileinput
import re

input_lines = list(fileinput.input())

cups = list(map(int, re.findall(r"\d", input_lines[0])))
number_of_cups = 1000000
number_of_moves = 10000000

succ = dict()
for (cup_index, cup) in enumerate(cups[:-1]):
    succ[cup] = cups[cup_index + 1]
succ[cups[-1]] = len(cups) + 1
for cup in range(len(cups) + 1, number_of_cups):
    succ[cup] = cup + 1
succ[number_of_cups] = cups[0]

source_cup = cups[0]
for move in range(number_of_moves):
    three_moving_cups = (
        succ[source_cup],
        succ[succ[source_cup]],
        succ[succ[succ[source_cup]]],
    )
    destination_cup = source_cup - 1 if source_cup != 1 else number_of_cups
    while destination_cup in three_moving_cups:
        destination_cup = (
            destination_cup - 1 if destination_cup != 1 else number_of_cups
        )
    succ[source_cup], succ[three_moving_cups[2]], succ[destination_cup] = (
        succ[three_moving_cups[2]],
        succ[destination_cup],
        three_moving_cups[0],
    )
    source_cup = succ[source_cup]
print(succ[1] * succ[succ[1]])
