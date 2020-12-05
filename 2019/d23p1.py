input_file = open("inputd23.txt", "r")
input_lines = input_file.readlines()

import collections
import copy

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

number_of_computers = 50
programs = [copy.deepcopy(program) for computer in range(number_of_computers)]
positions = [0] * number_of_computers
relative_bases = [0] * number_of_computers
outputs_computers = [[] for computer in range(number_of_computers)]
inputs_computers = [[] for computer in range(number_of_computers)]
input_indices = [0] * number_of_computers
network_addresses = list(range(number_of_computers))
first_input = [True] * number_of_computers
computer_done = [False] * number_of_computers

computer = 0
while not all(computer_done):
    while computer_done[computer]:
        computer = (computer + 1) % number_of_computers
    next_computer = False
    program = programs[computer]
    position = positions[computer]
    relative_base = relative_bases[computer]
    outputs = outputs_computers[computer]
    inputs = inputs_computers[computer]

    while position < len(program) and not next_computer:
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
            if first_input[computer]:
                input_parameter = network_addresses[computer]
                first_input[computer] = False
            else:
                if len(inputs) > 0:
                    input_parameter = inputs.pop(0)
                else:
                    input_parameter = -1
                    next_computer = True
            program[write_parameter_address] = input_parameter
        elif operation == 4:
            output_parameter = address[0]
            outputs.append(output_parameter)
            if len(outputs) % 3 == 0:
                if outputs[-3] == 255:
                    print(outputs[-1])
                    exit()
                else:
                    inputs_computers[outputs[-3]] += outputs[-2:]
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
            relative_bases[computer] = relative_base
        else:
            assert operation == 99
            computer_done[computer] = True
            next_computer = True
            break
        position += number_of_parameters[operation] + 1
        positions[computer] = position
        programs[computer] = program
        inputs_computers[computer] = inputs
        outputs_computers[computer] = outputs
    computer = (computer + 1) % number_of_computers
