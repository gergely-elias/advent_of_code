import fileinput

input_lines = list(fileinput.input())

head_position = (0, 0)
tail_position = head_position
visited_tail_positions = set([tail_position])

direction_mapping = {
    "D": (1, 0),
    "U": (-1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def sign(x):
    return (x > 0) - (x < 0)


for line in input_lines:
    command = line.strip().split()
    direction, amount = direction_mapping[command[0]], int(command[1])
    for _ in range(amount):
        head_position = tuple(
            [
                head_coord + direction_coord
                for head_coord, direction_coord in zip(head_position, direction)
            ]
        )
        direction_difference = tuple(
            [
                head_coord - tail_coord
                for head_coord, tail_coord in zip(head_position, tail_position)
            ]
        )
        tail_direction = (
            tuple(map(sign, direction_difference))
            if max(map(abs, direction_difference)) > 1
            else (0, 0)
        )
        tail_position = tuple(
            [
                tail_coord + direction_coord
                for tail_coord, direction_coord in zip(tail_position, tail_direction)
            ]
        )
        visited_tail_positions.add(tail_position)
print(len(visited_tail_positions))
