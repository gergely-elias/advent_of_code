import fileinput
import re
import copy

input_lines = list(fileinput.input())


def operate(instruction, registers, operator_index):
    reference = {"A": instruction[1], "B": instruction[2], "C": instruction[3]}
    if operator_index == 0:
        registers[reference["C"]] = (
            registers[reference["A"]] + registers[reference["B"]]
        )
    elif operator_index == 1:
        registers[reference["C"]] = registers[reference["A"]] + reference["B"]
    elif operator_index == 2:
        registers[reference["C"]] = (
            registers[reference["A"]] * registers[reference["B"]]
        )
    elif operator_index == 3:
        registers[reference["C"]] = registers[reference["A"]] * reference["B"]
    elif operator_index == 4:
        registers[reference["C"]] = (
            registers[reference["A"]] & registers[reference["B"]]
        )
    elif operator_index == 5:
        registers[reference["C"]] = registers[reference["A"]] & reference["B"]
    elif operator_index == 6:
        registers[reference["C"]] = (
            registers[reference["A"]] | registers[reference["B"]]
        )
    elif operator_index == 7:
        registers[reference["C"]] = registers[reference["A"]] | reference["B"]
    elif operator_index == 8:
        registers[reference["C"]] = registers[reference["A"]]
    elif operator_index == 9:
        registers[reference["C"]] = reference["A"]
    elif operator_index == 10:
        registers[reference["C"]] = (
            1 if reference["A"] > registers[reference["B"]] else 0
        )
    elif operator_index == 11:
        registers[reference["C"]] = (
            1 if registers[reference["A"]] > reference["B"] else 0
        )
    elif operator_index == 12:
        registers[reference["C"]] = (
            1 if registers[reference["A"]] > registers[reference["B"]] else 0
        )
    elif operator_index == 13:
        registers[reference["C"]] = (
            1 if reference["A"] == registers[reference["B"]] else 0
        )
    elif operator_index == 14:
        registers[reference["C"]] = (
            1 if registers[reference["A"]] == reference["B"] else 0
        )
    elif operator_index == 15:
        registers[reference["C"]] = (
            1 if registers[reference["A"]] == registers[reference["B"]] else 0
        )
    return registers


line_index = 0
result = 0
while input_lines[line_index].startswith("B"):
    registers_before_operation = list(
        map(int, re.findall("\d+", input_lines[line_index]))
    )
    instruction = list(map(int, re.findall("\d+", input_lines[line_index + 1])))
    registers_after_operation = list(
        map(int, re.findall("\d+", input_lines[line_index + 2]))
    )

    if [
        operate(instruction, copy.deepcopy(registers_before_operation), operator_index)
        for operator_index in range(16)
    ].count(registers_after_operation) >= 3:
        result += 1
    line_index += 4

print(result)
