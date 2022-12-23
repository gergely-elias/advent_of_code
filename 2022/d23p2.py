import fileinput
import collections
import copy

input_lines = list(fileinput.input())

elf_positions = []
for y, line in enumerate(input_lines):
    for x, char in enumerate(line.strip()):
        if char == "#":
            elf_positions.append((y, x))

number_of_rounds = 10
dimensions = 2

step_directions = [
    tuple(
        neighbour_value if coord_index == iter_index else 0
        for iter_index in range(dimensions)
    )
    for coord_index in range(dimensions)
    for neighbour_value in [-1, 1]
]
lookup_directions = {
    step_direction: [
        tuple(coord_surrounding if coord == 0 else coord for coord in step_direction)
        for coord_surrounding in [-1, 0, 1]
    ]
    for step_direction in step_directions
}
all_surrounding_directions = set.union(
    *[set(direction) for direction in lookup_directions.values()]
)


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


step = 0
prev_elf_positions = []
while elf_positions != prev_elf_positions:
    prev_elf_positions = elf_positions
    start_lookup_direction = step % len(lookup_directions)
    proposed_positions = []
    for elf_position in elf_positions:
        next_pos_candidate = copy.deepcopy(elf_position)
        if any(
            tuple_sum(elf_position, surronding_direction) in elf_positions
            for surronding_direction in all_surrounding_directions
        ):
            main_direction = step_directions[0]
            for step_direction_candidate in (
                step_directions[start_lookup_direction:]
                + step_directions[:start_lookup_direction]
            ):
                if not any(
                    tuple_sum(elf_position, lookup_direction) in elf_positions
                    for lookup_direction in lookup_directions[step_direction_candidate]
                ):
                    next_pos_candidate = tuple_sum(
                        elf_position, step_direction_candidate
                    )
                    break
        proposed_positions.append(next_pos_candidate)
    collision_positions = [
        position
        for position, count in collections.Counter(proposed_positions).items()
        if count > 1
    ]
    elf_positions = [
        original_position
        if proposed_position in collision_positions
        else proposed_position
        for original_position, proposed_position in zip(
            elf_positions, proposed_positions
        )
    ]
    step += 1

print(step)
