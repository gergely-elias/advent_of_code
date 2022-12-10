import fileinput

input_lines = list(fileinput.input())

instructions = []
for line in input_lines:
    instruction_split = line.strip().split()
    instruction = instruction_split[0], *map(int, instruction_split[1:])
    instructions.append(instruction)

x = 1
x_over_time = []
for instruction in instructions:
    if instruction[0] == "addx":
        instruction_completion_time = 2
        new_x = x + instruction[1]
    elif instruction[0] == "noop":
        instruction_completion_time = 1
        new_x = x
    x_over_time.extend([x for _ in range(instruction_completion_time)])
    x = new_x
x_over_time.append(x)

print(sum([cycle * x_over_time[cycle - 1] for cycle in range(20, 221, 40)]))
