import fileinput
import re

input_lines = list(fileinput.input())


def operate(instruction, registers):
    operation = instruction[0]
    reference = {"A": instruction[1], "B": instruction[2], "C": instruction[3]}
    if operation == "addr":
        registers[reference["C"]] = (
            registers[reference["A"]] + registers[reference["B"]]
        )
    elif operation == "addi":
        registers[reference["C"]] = registers[reference["A"]] + reference["B"]
    elif operation == "mulr":
        registers[reference["C"]] = (
            registers[reference["A"]] * registers[reference["B"]]
        )
    elif operation == "muli":
        registers[reference["C"]] = registers[reference["A"]] * reference["B"]
    elif operation == "banr":
        registers[reference["C"]] = (
            registers[reference["A"]] & registers[reference["B"]]
        )
    elif operation == "bani":
        registers[reference["C"]] = registers[reference["A"]] & reference["B"]
    elif operation == "borr":
        registers[reference["C"]] = (
            registers[reference["A"]] | registers[reference["B"]]
        )
    elif operation == "bori":
        registers[reference["C"]] = registers[reference["A"]] | reference["B"]
    elif operation == "setr":
        registers[reference["C"]] = registers[reference["A"]]
    elif operation == "seti":
        registers[reference["C"]] = reference["A"]
    elif operation == "gtir":
        registers[reference["C"]] = (
            1 if reference["A"] > registers[reference["B"]] else 0
        )
    elif operation == "gtri":
        registers[reference["C"]] = (
            1 if registers[reference["A"]] > reference["B"] else 0
        )
    elif operation == "gtrr":
        registers[reference["C"]] = (
            1 if registers[reference["A"]] > registers[reference["B"]] else 0
        )
    elif operation == "eqir":
        registers[reference["C"]] = (
            1 if reference["A"] == registers[reference["B"]] else 0
        )
    elif operation == "eqri":
        registers[reference["C"]] = (
            1 if registers[reference["A"]] == reference["B"] else 0
        )
    elif operation == "eqrr":
        registers[reference["C"]] = (
            1 if registers[reference["A"]] == registers[reference["B"]] else 0
        )
    return registers


instruction_pointer = int(re.findall(r"\d+", input_lines[0].strip())[0])
instruction_lines = [
    input_lines[line_index].strip() for line_index in range(1, len(input_lines))
]
instructions = [
    re.findall(r"[a-z]{4}", instruction_line)
    + list(map(int, re.findall(r"-?\d+", instruction_line)))
    for instruction_line in instruction_lines
]

index_of_halting_test_instruction = 28
registers = [0] * 6
while registers[instruction_pointer] in range(len(instructions)):
    operate(instructions[registers[instruction_pointer]], registers)
    if registers[instruction_pointer] == index_of_halting_test_instruction:
        print(registers[max(instructions[index_of_halting_test_instruction][1:3])])
        exit()
    registers[instruction_pointer] += 1
