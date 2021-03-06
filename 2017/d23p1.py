import fileinput
import re
import collections

input_lines = list(fileinput.input())

instructions = [line.strip().split() for line in input_lines]
registers = collections.defaultdict(lambda: 0)
instruction_index = 0
number_of_mul_instructions = 0


def substitute(value):
    if re.match(r"-?\d+", value):
        return int(value)
    return registers[value]


while instruction_index in range(0, len(instructions)):
    instruction = instructions[instruction_index]
    if instruction[0] == "set":
        registers[instruction[1]] = substitute(instruction[2])
    elif instruction[0] == "sub":
        registers[instruction[1]] -= substitute(instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] *= substitute(instruction[2])
        number_of_mul_instructions += 1
    elif instruction[0] == "jnz" and substitute(instruction[1]) != 0:
        instruction_index += substitute(instruction[2])
        continue
    instruction_index += 1

print(number_of_mul_instructions)
