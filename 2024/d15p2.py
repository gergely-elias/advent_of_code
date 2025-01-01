import fileinput

input_lines = list(fileinput.input())
warehouse_lines, instruction_lines = list(
    map(lambda x: x.split("\n"), "".join(input_lines).strip().split("\n\n"))
)
warehouse = [line.strip() for line in warehouse_lines]
instructions = "".join([line.strip() for line in instruction_lines])

width_multiplier = 2
height = len(warehouse)
width = width_multiplier * len(warehouse[0])

robot_position = None
walls = set()
boxes = set()
for y in range(height):
    for x in range(width // width_multiplier):
        if warehouse[y][x] == "#":
            for x_offset in range(width_multiplier):
                walls.add((y, width_multiplier * x + x_offset))
        elif warehouse[y][x] == "O":
            boxes.add((y, width_multiplier * x))
        elif warehouse[y][x] == "@":
            robot_position = (y, width_multiplier * x)


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


def push_directions_based_on_widths(a_width, b_width):
    return {
        (-1, 0): [(-1, x_offset) for x_offset in range(1 - b_width, a_width)],
        (0, 1): [(0, a_width)],
        (1, 0): [(1, x_offset) for x_offset in range(1 - b_width, a_width)],
        (0, -1): [(0, -b_width)],
    }


BOX_PUSH_WALL_DIRECTIONS = push_directions_based_on_widths(width_multiplier, 1)
BOX_PUSH_BOX_DIRECTIONS = push_directions_based_on_widths(
    width_multiplier, width_multiplier
)
ROBOT_PUSH_BOX_DIRECTIONS = push_directions_based_on_widths(1, width_multiplier)
ROBOT_PUSH_WALL_DIRECTIONS = push_directions_based_on_widths(1, 1)


def moves(coords, direction):
    boxes_to_push = []
    moveable_boxes = set()
    if any(
        tuple_sum(push_direction, coords) in walls
        for push_direction in ROBOT_PUSH_WALL_DIRECTIONS[direction]
    ):
        return (False, set())
    boxes_to_push.extend(
        push_coords
        for push_coords in (
            tuple_sum(push_direction, coords)
            for push_direction in ROBOT_PUSH_BOX_DIRECTIONS[direction]
        )
        if push_coords in boxes
    )
    while boxes_to_push:
        coords = boxes_to_push.pop()
        if coords not in moveable_boxes:
            moveable_boxes.add(coords)
            if any(
                tuple_sum(push_direction, coords) in walls
                for push_direction in BOX_PUSH_WALL_DIRECTIONS[direction]
            ):
                return (False, set())
            boxes_to_push.extend(
                push_coords
                for push_coords in (
                    tuple_sum(push_direction, coords)
                    for push_direction in BOX_PUSH_BOX_DIRECTIONS[direction]
                )
                if push_coords in boxes
            )
    return (True, moveable_boxes)


instruction_direction_mapping = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
for instruction in instructions:
    direction = instruction_direction_mapping[instruction]

    can_move, boxes_to_move = moves(robot_position, direction)
    if can_move:
        for b in boxes_to_move:
            boxes.remove(b)
        for b in boxes_to_move:
            boxes.add(tuple_sum(b, direction))
        robot_position = tuple_sum(robot_position, direction)

gps_total = 0
for box_y, box_x in boxes:
    gps_total += 100 * box_y + box_x
print(gps_total)
