input_file = open("inputd15.txt", "r")
input_lines = input_file.readlines()

import collections
import networkx

direction_commands = [1, 3, 2, 4]
direction_steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_direction = 0
droid_start_position = (0, 0)
paths = networkx.Graph()
droid_map = collections.defaultdict(lambda: " ")
oxygen_system_location = None
current_droid_position = droid_start_position

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
        input_parameter = direction_commands[current_direction]
        program[write_parameter_address] = input_parameter
    elif operation == 4:
        output_parameter = address[0]
        new_position = tuple(
            [
                current + step
                for (current, step) in zip(
                    current_droid_position, direction_steps[current_direction]
                )
            ]
        )
        if output_parameter == 0:
            droid_map[new_position] = "X"
            current_direction = (current_direction + 1) % 4
        else:
            paths.add_edge(current_droid_position, new_position)
            current_droid_position = new_position
            current_direction = (current_direction - 1) % 4
            droid_map[new_position] = "."
            undiscovered_area = False
            for y in range(
                min([discovered_cell[0] for discovered_cell in droid_map.keys()]),
                max([discovered_cell[0] for discovered_cell in droid_map.keys()]) + 1,
            ):
                for x in range(
                    min([discovered_cell[1] for discovered_cell in droid_map.keys()]),
                    max([discovered_cell[1] for discovered_cell in droid_map.keys()])
                    + 1,
                ):
                    current_cell = (y, x)
                    if droid_map[current_cell] == ".":
                        for lookaround_direction in direction_steps:
                            lookaround_cell = tuple(
                                [
                                    current + step
                                    for (current, step) in zip(
                                        current_cell, lookaround_direction
                                    )
                                ]
                            )
                            if droid_map[lookaround_cell] == " ":
                                undiscovered_area = True
                                break
                    if undiscovered_area:
                        break
                if undiscovered_area:
                    break
            if output_parameter == 2:
                oxygen_system_location = current_droid_position
            if not undiscovered_area:
                print(
                    max(
                        networkx.shortest_path_length(
                            paths, oxygen_system_location
                        ).values()
                    )
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
