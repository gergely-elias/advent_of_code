import fileinput

input_lines = list(fileinput.input())
enumerated_coordinates = list(
    enumerate([int(line.strip()) * 811589153 for line in input_lines])
)
number_of_coordinates = len(enumerated_coordinates)

for _ in range(10):
    for original_position_to_move in range(number_of_coordinates):
        for current_position, (original_position, coordinate) in enumerate(
            enumerated_coordinates
        ):
            if original_position == original_position_to_move:
                break
        enumerated_coordinates.pop(current_position)
        next_position = (current_position + coordinate) % (number_of_coordinates - 1)
        enumerated_coordinates = (
            enumerated_coordinates[:next_position]
            + [(original_position, coordinate)]
            + enumerated_coordinates[next_position:]
        )

for current_position, (original_position, coordinate) in enumerate(
    enumerated_coordinates
):
    if coordinate == 0:
        position_of_zero = current_position
        break

print(
    sum(
        enumerated_coordinates[(offset + position_of_zero) % number_of_coordinates][1]
        for offset in [1000, 2000, 3000]
    )
)
