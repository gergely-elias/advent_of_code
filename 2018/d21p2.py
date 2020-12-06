import fileinput

input_lines = list(fileinput.input())

instruction_lines = [
    input_lines[line_index].strip() for line_index in range(1, len(input_lines))
]
variables = [
    list(map(int, instruction_line.split()[1:]))
    for instruction_line in instruction_lines
]

init_helper = variables[6][1]
init_element = variables[7][0]
bitmasks = [variables[i][1] for i in [8, 10, 12]]
factor = variables[11][1]
threshold = variables[13][0]
divisor = variables[19][1]

element = 0
list_of_elements = []
while True:
    helper = init_helper | element
    element = init_element
    while True:
        element = (
            ((element + (helper & bitmasks[0])) & bitmasks[1]) * factor
        ) & bitmasks[2]
        if helper >= threshold:
            helper = helper // divisor
        else:
            break
    if element in list_of_elements:
        break
    else:
        list_of_elements.append(element)

print(list_of_elements[-1])
