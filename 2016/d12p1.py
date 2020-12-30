import fileinput

input_lines = list(fileinput.input())

registers = {"a": 0, "b": 0, "c": 0, "d": 0}

instructions = [line.strip().split() for line in input_lines]

pointer = 0
while 0 <= pointer < len(instructions):
    instruction, *params = instructions[pointer]
    if instruction == "cpy":
        if params[0] in registers:
            registers[params[1]] = registers[params[0]]
        else:
            registers[params[1]] = int(params[0])
        pointer += 1
    elif instruction == "inc":
        registers[params[0]] += 1
        pointer += 1
    elif instruction == "dec":
        registers[params[0]] -= 1
        pointer += 1
    elif instruction == "jnz":
        if params[0] in registers:
            if registers[params[0]] != 0:
                pointer += int(params[1])
            else:
                pointer += 1
        else:
            if int(params[0]) != 0:
                pointer += int(params[1])
            else:
                pointer += 1
    else:
        assert False
print(registers["a"])
