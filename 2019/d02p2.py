input_file = open("inputd02.txt", "r")
input_lines = input_file.readlines()

original_program = list(map(int, input_lines[0].split(",")))

for noun in range(100):
    for verb in range(100):
        program = original_program[:]
        program[1] = noun
        program[2] = verb

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
        if program[0] == 19690720:
            print(100 * noun + verb)
            exit()
