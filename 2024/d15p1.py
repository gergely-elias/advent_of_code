import fileinput

input_lines = list(fileinput.input())
warehouse_lines, instruction_lines = list(
    map(lambda x: x.split("\n"), "".join(input_lines).strip().split("\n\n"))
)
warehouse = [line.strip() for line in warehouse_lines]
instructions = "".join([line.strip() for line in instruction_lines])

height = len(warehouse)
width = len(warehouse[0])

robot_position = None
walls = set()
boxes = set()
for y in range(height):
    for x in range(width):
        if warehouse[y][x] == "#":
            walls.add((y, x))
        elif warehouse[y][x] == "O":
            boxes.add((y, x))
        elif warehouse[y][x] == "@":
            robot_position = (y, x)


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


INSTRUCTION_DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
for instruction in instructions:
    direction = INSTRUCTION_DIRECTIONS[instruction]
    next_robot_position_candidate = tuple_sum(robot_position, direction)
    if next_robot_position_candidate in walls:
        pass
    elif next_robot_position_candidate in boxes:
        box_loop_position = next_robot_position_candidate
        while box_loop_position in boxes:
            box_loop_position = tuple_sum(box_loop_position, direction)
        if box_loop_position in walls:
            pass
        else:
            boxes.add(box_loop_position)
            boxes.remove(next_robot_position_candidate)
            robot_position = next_robot_position_candidate
    else:
        robot_position = next_robot_position_candidate

gps_total = 0
for y, x in boxes:
    gps_total += 100 * y + x
print(gps_total)
