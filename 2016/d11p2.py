import fileinput
import re
import heapq
import itertools

input_lines = list(fileinput.input())

ordinals = ["first", "second", "third", "fourth"]
elevator_position = 0
generator_positions = dict()
microchip_positions = dict()
rocks = set()
seen_setups = set()
for line in input_lines:
    floor_description = line.strip()
    floor_ordinal = re.search(r"The\ (\w+)\ floor", floor_description).groups()[0]
    generators = re.findall(r"(\w+)\ generator", floor_description)
    microchips = re.findall(r"(\w+)-compatible microchip", floor_description)
    floor_index = ordinals.index(floor_ordinal)
    for generator in generators:
        generator_positions[generator] = floor_index
    for microchip in microchips:
        microchip_positions[microchip] = floor_index
    rocks.update(set.union(set(generators), set(microchips)))
for rock in ["elerium", "dilithium"]:
    generator_positions[rock] = 0
    microchip_positions[rock] = 0
    rocks.add(rock)
rocks_as_list = list(rocks)
number_of_rocks = len(rocks_as_list)
setup = tuple(
    [elevator_position]
    + sorted(
        [
            (generator_positions[rock], microchip_positions[rock])
            for rock in rocks_as_list
        ]
    )
)

heap_entry_id = 0
states = [(0, heap_entry_id, setup)]
heap_entry_id += 1
while len(states) > 0:
    total_steps, _, state_to_process = heapq.heappop(states)
    if state_to_process in seen_setups:
        continue
    seen_setups.add(state_to_process)
    elevator_position, generator_positions, microchip_positions = (
        state_to_process[0],
        [
            state_to_process[rock_index][0]
            for rock_index in range(1, number_of_rocks + 1)
        ],
        [
            state_to_process[rock_index][1]
            for rock_index in range(1, number_of_rocks + 1)
        ],
    )
    if [elevator_position] + generator_positions + microchip_positions == [
        len(ordinals) - 1
    ] * (2 * number_of_rocks + 1):
        print(total_steps)
        break
    if elevator_position in (generator_positions + microchip_positions) and all(
        [
            microchip_positions[index] == generator_positions[index]
            or microchip_positions[index] not in generator_positions
            for index in range(number_of_rocks)
        ]
    ):
        item_positions = generator_positions + microchip_positions
        matching_indices = [
            item_index
            for item_index, item_position in enumerate(item_positions)
            if item_position == elevator_position
        ]
        possible_next_floors = []
        if elevator_position < len(ordinals) - 1:
            possible_next_floors.append(elevator_position + 1)
        if elevator_position > 0:
            possible_next_floors.append(elevator_position - 1)
        for next_floor in possible_next_floors:
            for number_of_moving_items in range(1, 3):
                for moving_items in itertools.combinations(
                    matching_indices, number_of_moving_items
                ):
                    new_item_positions = item_positions[:]
                    for moving_item in moving_items:
                        new_item_positions[moving_item] = next_floor
                    heapq.heappush(
                        states,
                        (
                            total_steps + 1,
                            heap_entry_id,
                            tuple(
                                [next_floor]
                                + sorted(
                                    list(
                                        zip(
                                            new_item_positions[:number_of_rocks],
                                            new_item_positions[number_of_rocks:],
                                        )
                                    )
                                )
                            ),
                        ),
                    )
                    heap_entry_id += 1
