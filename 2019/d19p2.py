input_file = open("inputd19.txt", "r")
input_lines = input_file.readlines()

import collections

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
input_parameter_index = 0
inputs = []

size = 100
right_edge_x = dict()
left_edge_x = dict()
looking_for_top_left_corner = True
top_left_x = 0
top_left_y = 0
right_edge = True

while True:
    in_beam = False
    program = collections.defaultdict(lambda: 0)
    for memory_index, code in enumerate(orig_program):
        program[memory_index] = code
    position = 0
    relative_base = 0
    if looking_for_top_left_corner:
        if top_left_x == 0:
            top_left_x, top_left_y = top_left_y + 1, 0
        else:
            top_left_x, top_left_y = top_left_x - 1, top_left_y + 1
        inputs.append(top_left_y)
        inputs.append(top_left_x)
    elif right_edge:
        inputs.append(right_y)
        inputs.append(right_x)
    else:
        inputs.append(left_y)
        inputs.append(left_x)

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
            input_parameter = inputs[input_parameter_index]
            program[write_parameter_address] = input_parameter
            input_parameter_index += 1
        elif operation == 4:
            output_parameter = address[0]
            in_beam = output_parameter == 1
            if looking_for_top_left_corner:
                if in_beam:
                    right_y = top_left_y
                    right_x = top_left_x
                    left_y = top_left_y
                    left_x = top_left_x
                    looking_for_top_left_corner = False
            else:
                if right_edge:
                    if in_beam:
                        right_x += 1
                    else:
                        right_edge_x[right_y] = right_x - 1
                        right_y += 1
                else:
                    if in_beam:
                        left_edge_x[left_y] = left_x
                        left_y += 1
                    else:
                        left_x += 1
                right_edge = not right_edge
                square_bottom_left_y = min(left_y - 1, right_y - 1)
                if square_bottom_left_y >= size + top_left_y - 1:
                    if (
                        right_edge_x[square_bottom_left_y - size + 1]
                        - left_edge_x[square_bottom_left_y]
                        + 1
                        >= size
                    ):
                        print(
                            (square_bottom_left_y - size + 1) * 10000
                            + left_edge_x[square_bottom_left_y]
                        )
                        exit()
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
