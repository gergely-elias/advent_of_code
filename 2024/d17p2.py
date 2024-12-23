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


initial_registers = {}
for line in input_lines:
    match_register = re.match(r"^Register ([A-C]): (\d+)$", line.strip())
    if match_register:
        register_as_string, value_as_string = match_register.groups()
        initial_registers[RegisterNames[register_as_string]] = int(value_as_string)
        continue
    match_program = re.match(r"^Program: ([\d,]+)$", line.strip())
    if match_program:
        program = list(map(int, match_program.groups()[0].split(",")))


def combo(operand, registers):
    if operand < 4:
        return operand
    if operand < 7:
        return registers[list(RegisterNames)[operand - 4]]
    raise ValueError("reserved combo operand", operand)


def run_program(initial_value):
    registers = initial_registers
    registers[RegisterNames.A] = initial_value
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
                    2 ** combo(operand, registers)
                )
            case Opcodes.bxl:
                registers[RegisterNames.B] = registers[RegisterNames.B] ^ operand
            case Opcodes.bst:
                registers[RegisterNames.B] = combo(operand, registers) % 8
            case Opcodes.jnz:
                if registers[RegisterNames.A] != 0:
                    instruction_pointer = operand
            case Opcodes.bxc:
                registers[RegisterNames.B] = (
                    registers[RegisterNames.B] ^ registers[RegisterNames.C]
                )
            case Opcodes.out:
                output.append(combo(operand, registers) % 8)
            case Opcodes.bdv:
                registers[RegisterNames.B] = registers[RegisterNames.A] // (
                    2 ** combo(operand, registers)
                )
            case Opcodes.cdv:
                registers[RegisterNames.C] = registers[RegisterNames.A] // (
                    2 ** combo(operand, registers)
                )
    return output


def convert_to_octal(octal_digits):
    return sum(digit * 8**place for place, digit in enumerate(octal_digits))


suffices = [()]
for number_of_digits in range(len(program)):
    next_suffices = []
    for suffix in suffices:
        for next_digit in range(8):
            next_suffix = (next_digit,) + suffix
            output = run_program(convert_to_octal(next_suffix))
            if output == program[-len(output) :]:
                next_suffices.append(next_suffix)
    suffices = next_suffices

print(convert_to_octal(min(suffices)))
