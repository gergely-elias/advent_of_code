import fileinput

input_lines = list(fileinput.input())
height = len(input_lines)
width = len(input_lines[0].strip())
step_directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
blizzard_directions = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}
walls = []
blizzards = []
for y, line in enumerate(input_lines):
    for x, char in enumerate(line.strip()):
        if char == "#":
            walls.append((y, x))
        elif char != ".":
            blizzards.append(((y, x), blizzard_directions[char]))


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


def wrap_blizzard(potential_wall_position):
    assert potential_wall_position not in [(0, 1), (height - 1, width - 2)]
    y, x = potential_wall_position
    y = (y - 1) % (height - 2) + 1
    x = (x - 1) % (width - 2) + 1
    return y, x


step = 0
start_position = (0, 1)
for end_position in [(height - 1, width - 2), (0, 1), (height - 1, width - 2)]:
    possible_positions = set([start_position])
    while end_position not in possible_positions:
        step += 1
        blizzards = [
            (wrap_blizzard(tuple_sum(*blizzard)), blizzard[1]) for blizzard in blizzards
        ]
        blizzard_positions = set(newblizzard[0] for newblizzard in blizzards)
        excluded_positions = blizzard_positions.union(walls).union(
            [(-1, 1), (height, width - 2)]
        )
        all_positions = set(
            tuple_sum(position, step_direction)
            for position in possible_positions
            for step_direction in step_directions
        )
        possible_positions = all_positions.difference(excluded_positions)
    start_position = end_position
print(step)
