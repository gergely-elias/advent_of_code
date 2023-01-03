import fileinput
import re

input_lines = list(fileinput.input())
map_lines = [line.strip("\n") for line in input_lines[:-2]]
instructions = input_lines[-1].strip()

height = len(map_lines)
width = max(len(line) for line in map_lines)

mymap = [list(line + " " * (width - len(line))) for line in map_lines]

start_position = None
for x, char in enumerate(map_lines[0]):
    if char == ".":
        start_position = (0, x)
        break

facing = 0
directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


def tuple_scale(mytuple, factor):
    return tuple(factor * coord for coord in mytuple)


assert instructions[0] not in "LR"
assert instructions[-1] not in "LR"
instructions += "N"

position = start_position
for path_fragment in re.findall(r"\d+[LNR]", instructions):
    amount = int(path_fragment[:-1])
    turn = path_fragment[-1]
    for _ in range(amount):
        next_position_y, next_position_x = tuple_sum(position, directions[facing])
        next_position_y, next_position_x = (
            next_position_y % height,
            next_position_x % width,
        )
        while mymap[next_position_y][next_position_x] == " ":
            next_position_y, next_position_x = tuple_sum(
                (next_position_y, next_position_x), directions[facing]
            )
            next_position_y, next_position_x = (
                next_position_y % height,
                next_position_x % width,
            )
        if mymap[next_position_y][next_position_x] == "#":
            break
        else:
            position = (next_position_y, next_position_x)

    facing = (facing + "LNR".index(turn) - 1) % len(directions)

print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + facing)
