import fileinput

input_lines = list(fileinput.input())


def parse_line(line):
    operation, argument = line.split()
    return (operation, int(argument))


def replace(instruction):
    operation, argument = instruction
    if operation == "jmp":
        return (True, ("nop", argument))
    elif operation == "nop":
        return (True, ("jmp", argument))
    else:
        return (False, instruction)


original_instructions = [parse_line(line.strip()) for line in input_lines]

for replaced_instruction_index in range(len(original_instructions)):
    is_replaced, replaced_instruction = replace(
        original_instructions[replaced_instruction_index]
    )
    if not is_replaced:
        continue
    instructions = original_instructions[:]
    instructions[replaced_instruction_index] = replaced_instruction

    accumulator = 0
    current_instruction_index = 0
    executed_instructions = set()

    while current_instruction_index < len(instructions):
        current_operation, current_argument = instructions[current_instruction_index]
        if current_instruction_index in executed_instructions:
            break
        executed_instructions.add(current_instruction_index)
        if current_operation == "acc":
            accumulator += current_argument
            current_instruction_index += 1
        elif current_operation == "jmp":
            current_instruction_index += current_argument
        elif current_operation == "nop":
            current_instruction_index += 1
    if current_instruction_index == len(instructions):
        print(accumulator)
        exit()
