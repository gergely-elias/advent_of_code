import enum
import fileinput
import re

input_lines = list(fileinput.input())


class RegisterNames(enum.Enum):
    A = enum.auto()
    B = enum.auto()
    C = enum.auto()


class Opcodes(enum.Enum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


registers = {}
for line in input_lines:
    match_register = re.match(r"^Register ([A-C]): (\d+)$", line.strip())
    if match_register:
        register_as_string, value_as_string = match_register.groups()
        registers[RegisterNames[register_as_string]] = int(value_as_string)
        continue
    match_program = re.match(r"^Program: ([\d,]+)$", line.strip())
    if match_program:
        program = list(map(int, match_program.groups()[0].split(",")))


def combo(operand):
    if operand < 4:
        return operand
    if operand < 7:
        return registers[list(RegisterNames)[operand - 4]]
    raise ValueError("reserved combo operand", operand)


instruction_pointer = 0
output = []
while instruction_pointer in range(len(program)):
    opcode = Opcodes(program[instruction_pointer])
    instruction_pointer += 1
    operand = program[instruction_pointer]
    instruction_pointer += 1
    match opcode:
        case Opcodes.adv:
            registers[RegisterNames.A] = registers[RegisterNames.A] // (
                2 ** combo(operand)
            )
        case Opcodes.bxl:
            registers[RegisterNames.B] = registers[RegisterNames.B] ^ operand
        case Opcodes.bst:
            registers[RegisterNames.B] = combo(operand) % 8
        case Opcodes.jnz:
            if registers[RegisterNames.A] != 0:
                instruction_pointer = operand
        case Opcodes.bxc:
            registers[RegisterNames.B] = (
                registers[RegisterNames.B] ^ registers[RegisterNames.C]
            )
        case Opcodes.out:
            output.append(combo(operand) % 8)
        case Opcodes.bdv:
            registers[RegisterNames.B] = registers[RegisterNames.A] // (
                2 ** combo(operand)
            )
        case Opcodes.cdv:
            registers[RegisterNames.C] = registers[RegisterNames.A] // (
                2 ** combo(operand)
            )

print(",".join(map(str, output)))