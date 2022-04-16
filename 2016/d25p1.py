import fileinput

input_lines = list(fileinput.input())

instructions = [line.strip().split() for line in input_lines]

register_a_init = 1
while True:
    registers = {"a": register_a_init, "b": 0, "c": 0, "d": 0}
    pointer = 0
    outputs = []
    states = {0: [], 1: []}
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
        elif instruction == "out":
            if params[0] in registers:
                output = registers[params[0]]
            else:
                output = int(params[0])
            if output != len(outputs) % 2:
                break
            else:
                outputs.append(output)
                if registers in states[output]:
                    print(register_a_init)
                    exit()
                states[output].append(registers.copy())
            pointer += 1
        else:
            assert False
    register_a_init += 1
