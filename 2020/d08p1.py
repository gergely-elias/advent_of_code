import fileinput
import collections
import networkx
import re

input_lines = list(fileinput.input())


def parse_line(line):
    operation, argument = line.split()
    return (operation, int(argument))


instructions = [parse_line(line.strip()) for line in input_lines]
accumulator = 0
current_instruction_index = 0
executed_instructions = set()

while current_instruction_index < len(instructions):
    current_operation, current_argument = instructions[current_instruction_index]
    if current_instruction_index in executed_instructions:
        print(accumulator)
        exit()
    executed_instructions.add(current_instruction_index)
    if current_operation == "acc":
        accumulator += current_argument
        current_instruction_index += 1
    elif current_operation == "jmp":
        current_instruction_index += current_argument
    elif current_operation == "nop":
        current_instruction_index += 1
