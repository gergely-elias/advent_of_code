import fileinput
import collections

input_lines = list(fileinput.input())

orig_program = list(map(int, input_lines[0].split(",")))
program = collections.defaultdict(lambda: 0)
for memory_index, code in enumerate(orig_program):
    program[memory_index] = code

operation_scheme = {
    1: "rrw",
    2: "rrw",
    3: "w",
    4: "r",
    5: "rr",
    6: "rr",
    7: "rrw",
    8: "rrw",
    9: "r",
    99: "",
}

number_of_parameters = {op: len(operation_scheme[op]) for op in operation_scheme}
addressable_length = {op: operation_scheme[op].count("r") for op in operation_scheme}
write_parameter_index = {
    op: operation_scheme[op].index("w") if "w" in operation_scheme[op] else None
    for op in operation_scheme
}

position = 0
relative_base = 0
input_index = 0
inputs = []
output_line = ""
doors = []
items = []
reading_doors = False
reading_items = False
while position < len(program):
    operation_with_mode_indicators = program[position]
    operation = operation_with_mode_indicators % 100
    mode_indicators = [
        (operation_with_mode_indicators // (10 ** decimal_place)) % 10
        for decimal_place in [2, 3, 4]
    ]
    opcode_parameters = [
        program[x]
        for x in range(position + 1, position + number_of_parameters[operation] + 1)
    ]
    address = {}
    for index in range(addressable_length[operation]):
        if mode_indicators[index] == 1:
            address[index] = opcode_parameters[index]
        else:
            assert mode_indicators[index] in [0, 2]
            address[index] = program[
                opcode_parameters[index]
                + (relative_base if mode_indicators[index] == 2 else 0)
            ]
    write_parameter_address = (
        None
        if write_parameter_index[operation] is None
        else opcode_parameters[write_parameter_index[operation]]
        + (
            relative_base
            if mode_indicators[write_parameter_index[operation]] == 2
            else 0
        )
    )

    if operation == 1:
        program[write_parameter_address] = address[0] + address[1]
    elif operation == 2:
        program[write_parameter_address] = address[0] * address[1]
    elif operation == 3:
        if input_index == len(inputs):
            doors = []
            items = []
            input_parameter = input() + "\n"
            inputs.extend([int(ord(x)) for x in input_parameter])
        program[write_parameter_address] = inputs[input_index]
        input_index += 1
    elif operation == 4:
        output_parameter = address[0]
        output_chr = chr(output_parameter)
        if output_chr == "\n":
            if output_line == "":
                reading_doors = False
                reading_items = False
            if reading_doors:
                doors.append(output_line[2:])
            elif reading_items:
                items.append(output_line[2:])
            if output_line == "Doors here lead:":
                reading_doors = True
            elif output_line == "Items here:":
                reading_items = True
            print(output_line)
            output_line = ""
        else:
            output_line += output_chr
    elif operation == 5:
        if address[0] != 0:
            position = address[1]
            continue
    elif operation == 6:
        if address[0] == 0:
            position = address[1]
            continue
    elif operation == 7:
        program[write_parameter_address] = 1 if address[0] < address[1] else 0
    elif operation == 8:
        program[write_parameter_address] = 1 if address[0] == address[1] else 0
    elif operation == 9:
        relative_base += address[0]
    else:
        assert operation == 99
        break
    position += number_of_parameters[operation] + 1
