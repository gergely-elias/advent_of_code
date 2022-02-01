import fileinput

input_lines = list(fileinput.input())

registers = {"a": 1, "b": 0}
line_index = 0
while line_index < len(input_lines):
    command = input_lines[line_index].strip().split(" ")
    offset = 1
    if command[0] == "hlf":
        registers[command[1]] //= 2
    elif command[0] == "tpl":
        registers[command[1]] *= 3
    elif command[0] == "inc":
        registers[command[1]] += 1
    elif command[0] == "jmp":
        offset = int(command[1])
    elif command[0] == "jie":
        if registers[command[1][:-1]] % 2 == 0:
            offset = int(command[2])
    elif command[0] == "jio":
        if registers[command[1][:-1]] == 1:
            offset = int(command[2])
    else:
        break
    line_index += offset

print(registers["b"])
