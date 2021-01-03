import fileinput
import collections
import re

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
items_in_room = []
inventory = []
reading_doors = False
reading_items_in_room = False
reading_inventory = False
room_name = ""
room_directions_to_go = [""]
room_directions_discovered = []
current_room_direction = ""
weighting_turn = True
weighing_attempt_index = 0
direction_inputs = {"e": "east", "s": "south", "w": "west", "n": "north"}
opposing_direction = {"e": "w", "s": "n", "w": "e", "n": "s"}

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
            takeable_items_in_room = set(items_in_room).difference(
                {
                    "escape pod",
                    "giant electromagnet",
                    "molten lava",
                    "infinite loop",
                    "photons",
                }
            )
            if len(takeable_items_in_room) > 0 and len(room_directions_to_go) > 0:
                takeable_item = takeable_items_in_room.pop()
                input_parameter = "take " + takeable_item
            else:
                input_parameter = None
                while input_parameter is None and len(room_directions_to_go) > 0:
                    next_room_direction_to_go = room_directions_to_go[0]
                    if current_room_direction == next_room_direction_to_go:
                        if room_name == "Security Checkpoint":
                            if current_room_direction not in room_directions_discovered:
                                room_directions_to_go = room_directions_to_go + [
                                    current_room_direction
                                ]
                            else:
                                fixed_order_of_items = tuple(inventory[:])
                                door_towards_goal = direction_inputs[
                                    [
                                        door[0]
                                        for door in doors
                                        if door[0]
                                        != opposing_direction[
                                            current_room_direction[-1]
                                        ]
                                    ][0]
                                ]
                        else:
                            for door in doors:
                                if (
                                    len(current_room_direction) == 0
                                    or door[0]
                                    != opposing_direction[current_room_direction[-1]]
                                ):
                                    room_directions_to_go = [
                                        current_room_direction + door[0]
                                    ] + room_directions_to_go
                        room_directions_to_go.remove(current_room_direction)
                        room_directions_discovered.append(current_room_direction)
                    elif next_room_direction_to_go.startswith(current_room_direction):
                        step_direction = next_room_direction_to_go[
                            len(current_room_direction)
                        ]
                        input_parameter = direction_inputs[step_direction]
                        current_room_direction = current_room_direction + step_direction
                    else:
                        input_parameter = direction_inputs[
                            opposing_direction[current_room_direction[-1]]
                        ]
                        current_room_direction = current_room_direction[:-1]
                if input_parameter is None:
                    if weighting_turn:
                        input_parameter = door_towards_goal
                        weighing_attempt_index += 1
                    else:
                        item_to_modify = fixed_order_of_items[
                            list(
                                reversed(
                                    list(
                                        (
                                            "0" * (len(fixed_order_of_items) - 1)
                                            + bin(weighing_attempt_index)[2:]
                                        )[-len(fixed_order_of_items) :]
                                    )
                                )
                            ).index("1")
                        ]
                        if item_to_modify in inventory:
                            input_parameter = "drop " + item_to_modify
                        else:
                            input_parameter = "take " + item_to_modify
                    weighting_turn = not weighting_turn
            if input_parameter in doors:
                doors = []
                items_in_room = []
            elif input_parameter.startswith("take "):
                item_to_take = input_parameter[5:]
                if item_to_take in items_in_room:
                    items_in_room.remove(item_to_take)
                    inventory.append(item_to_take)
            elif input_parameter.startswith("drop"):
                item_to_drop = input_parameter[5:]
                if item_to_drop in inventory:
                    inventory.remove(item_to_drop)
                    items_in_room.append(item_to_drop)
            elif input_parameter == "inv":
                inventory = []
            inputs.extend([int(ord(x)) for x in input_parameter + "\n"])
        program[write_parameter_address] = inputs[input_index]
        input_index += 1
    elif operation == 4:
        output_parameter = address[0]
        output_chr = chr(output_parameter)
        if output_chr == "\n":
            if output_line == "":
                reading_doors = False
                reading_items_in_room = False
                reading_inventory = False
            if reading_doors:
                doors.append(output_line[2:])
            elif reading_items_in_room:
                items_in_room.append(output_line[2:])
            elif reading_inventory:
                inventory.append(output_line[2:])
            if output_line == "Doors here lead:":
                reading_doors = True
            elif output_line == "Items here:":
                reading_items_in_room = True
            elif output_line == "Items in your inventory:":
                reading_inventory = True
            elif output_line.startswith("=="):
                room_name = output_line[3:-3]
            elif output_line.endswith("you are ejected back to the checkpoint."):
                doors = []
            else:
                digits = re.search(
                    r"You should be able to get in by typing (\d+) on the keypad",
                    output_line,
                )
                if digits is not None:
                    print(digits.groups()[0])
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
