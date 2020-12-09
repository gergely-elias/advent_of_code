import fileinput
import networkx

input_lines = list(fileinput.input())


def parse_line(line):
    operation, argument = line.split()
    return (operation, int(argument))


instructions = [parse_line(line.strip()) for line in input_lines]

instruction_flow = networkx.DiGraph()
for instruction_index, instruction in enumerate(instructions):
    instruction_operation, instruction_argument = instruction
    next_instruction_index = instruction_index + (
        instruction_argument if instruction_operation == "jmp" else 1
    )
    if next_instruction_index < 0 or next_instruction_index > len(instructions):
        next_instruction_index = -1
    instruction_flow.add_edge(instruction_index, next_instruction_index)

halting_indices = networkx.bfs_tree(instruction_flow, len(instructions), reverse=True)

current_instruction_index = 0
accumulator = 0
change_happened = False
change_operation = {"nop": "jmp", "jmp": "nop"}
while current_instruction_index < len(instructions):
    current_operation, current_argument = instructions[current_instruction_index]
    if not change_happened and current_operation in change_operation:
        next_instruction_index_changed = current_instruction_index + (
            current_argument if change_operation[current_operation] == "jmp" else 1
        )
        if next_instruction_index_changed in halting_indices:
            current_instruction_index = next_instruction_index_changed
            change_happened = True
            continue
    if current_operation == "acc":
        accumulator += current_argument
        current_instruction_index += 1
    elif current_operation == "jmp":
        current_instruction_index += current_argument
    elif current_operation == "nop":
        current_instruction_index += 1
print(accumulator)
