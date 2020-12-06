import fileinput

input_lines = list(fileinput.input())

program = list(map(int, input_lines[0].split(",")))
program[1] = 12
program[2] = 2

opcode_length = 4
for position in range(0, len(program), opcode_length):
    opcode = program[position : position + opcode_length]
    operation = opcode[0]
    input1 = program[opcode[1]]
    input2 = program[opcode[2]]
    if operation == 1:
        result = input1 + input2
    elif operation == 2:
        result = input1 * input2
    else:
        break
    program[opcode[3]] = result

print(program[0])
