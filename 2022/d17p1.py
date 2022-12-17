import fileinput

input_lines = list(fileinput.input())


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


jet_pattern = input_lines[0].strip()
number_of_rocks = 2022
chamber_width = 7
tower_height = 0
taken_positions = set()
rock_types = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]
jet_char_to_direction = {
    ">": (1, 0),
    "<": (-1, 0),
}
fall_direction = (0, -1)

jet_index = 0
for rock_index in range(number_of_rocks):
    rock_shape = rock_types[rock_index % len(rock_types)]
    rock_position = [
        tuple_sum((2, 3 + tower_height), rock_part) for rock_part in rock_shape
    ]
    rock_landed = False
    while not rock_landed:
        jet_direction = jet_char_to_direction[jet_pattern[jet_index % len(jet_pattern)]]
        next_rock_position = [
            tuple_sum(jet_direction, rock_part) for rock_part in rock_position
        ]
        if not any(
            [
                rock_part_position[0] < 0
                or rock_part_position[0] >= chamber_width
                or rock_part_position in taken_positions
                for rock_part_position in next_rock_position
            ]
        ):
            rock_position = next_rock_position
        next_rock_position = [
            tuple_sum(fall_direction, rock_part) for rock_part in rock_position
        ]
        if any(
            [
                rock_part_position in taken_positions or rock_part_position[1] < 0
                for rock_part_position in next_rock_position
            ]
        ):
            taken_positions.update(rock_position)
            tower_height = max(
                tower_height,
                *[rock_part_position[1] + 1 for rock_part_position in rock_position]
            )
            rock_landed = True
        else:
            rock_position = next_rock_position
        jet_index += 1
print(tower_height)
