import fileinput

input_lines = list(fileinput.input())

registers = {"a": 7, "b": 0, "c": 0, "d": 0}

instructions = [line.strip().split() for line in input_lines]

pointer = 0
while 0 <= pointer < len(instructions):
    instruction, *params = instructions[pointer]
    if instruction == "cpy":
        if params[1] in registers:
            if params[0] in registers:
                registers[params[1]] = registers[params[0]]
            else:
                registers[params[1]] = int(params[0])
        pointer += 1
    elif instruction == "inc":
        if params[0] in registers:
            registers[params[0]] += 1
        pointer += 1
    elif instruction == "dec":
        if params[0] in registers:
            registers[params[0]] -= 1
        pointer += 1
    elif instruction == "jnz":
        if params[0] in registers:
            if registers[params[0]] != 0:
                if params[1] in registers:
                    pointer += registers[params[1]]
                else:
                    pointer += int(params[1])
            else:
                pointer += 1
        else:
            if int(params[0]) != 0:
                if params[1] in registers:
                    pointer += registers[params[1]]
                else:
                    pointer += int(params[1])
            else:
                pointer += 1
    elif instruction == "tgl":
        if params[0] in registers:
            toggle_pointer = pointer + registers[params[0]]
        else:
            toggle_pointer = pointer + int(params[0])
        if 0 <= toggle_pointer < len(instructions):
            if len(instructions[toggle_pointer]) == 2:
                if instructions[toggle_pointer][0] == "inc":
                    instructions[toggle_pointer][0] = "dec"
                else:
                    instructions[toggle_pointer][0] = "inc"
            elif len(instructions[toggle_pointer]) == 3:
                if instructions[toggle_pointer][0] == "jnz":
                    instructions[toggle_pointer][0] = "cpy"
                else:
                    instructions[toggle_pointer][0] = "jnz"
        pointer += 1
    else:
        assert False
print(registers["a"])
