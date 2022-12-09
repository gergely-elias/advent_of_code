import fileinput

input_lines = list(fileinput.input())

number_of_knots = 10
positions = [(0, 0) for _ in range(number_of_knots)]
visited_tail_positions = set([positions[number_of_knots - 1]])

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
        positions[0] = tuple(
            [
                head_coord + direction_coord
                for head_coord, direction_coord in zip(positions[0], direction)
            ]
        )
        for knot_index in range(number_of_knots - 1):
            direction_difference = tuple(
                [
                    current_knot_coord - next_knot_coord
                    for current_knot_coord, next_knot_coord in zip(
                        positions[knot_index], positions[knot_index + 1]
                    )
                ]
            )
            next_knot_direction = (
                tuple(map(sign, direction_difference))
                if max(map(abs, direction_difference)) > 1
                else (0, 0)
            )
            positions[knot_index + 1] = tuple(
                [
                    next_knot_coord + direction_coord
                    for next_knot_coord, direction_coord in zip(
                        positions[knot_index + 1], next_knot_direction
                    )
                ]
            )
        visited_tail_positions.add(positions[number_of_knots - 1])
print(len(visited_tail_positions))
