import fileinput
import re

input_lines = list(fileinput.input())

cups = list(map(int, re.findall("\d", input_lines[0])))
number_of_cups = len(cups)

for move in range(100):
    source_cup = cups[0]
    three_moving_cups = [cups.pop(1), cups.pop(1), cups.pop(1)]
    destination_cup = source_cup - 1 if source_cup != 1 else number_of_cups
    while destination_cup not in cups:
        destination_cup = (
            destination_cup - 1 if destination_cup != 1 else number_of_cups
        )
    destination_cup_index = cups.index(destination_cup)
    cups = (
        cups[: destination_cup_index + 1]
        + three_moving_cups
        + cups[destination_cup_index + 1 :]
    )
    cups = cups[1:] + cups[:1]
cup1_index = cups.index(1)
print("".join(map(str, cups[cup1_index + 1 :] + cups[:cup1_index])))
