import fileinput
import heapq

input_lines = list(fileinput.input())
amphibian_types = "ABCD"
pit_columns = [
    2 * amphibian_index + 3 for amphibian_index in range(len(amphibian_types))
]
parking_columns = list(
    set(range(1, 2 * len(amphibian_types) + 4)).difference(pit_columns)
)
init_pits = tuple(
    tuple(
        input_lines[line_index][column_index]
        for line_index in range(2, len(input_lines) - 1)
    )
    for column_index in pit_columns
)
init_hallway = tuple(input_lines[1][column_index] for column_index in parking_columns)
augmentation = (("D", "D"), ("C", "B"), ("B", "A"), ("A", "C"))
init_pits = tuple(
    (pit_init[0], *pit_augmentation, *pit_init[1:])
    for pit_init, pit_augmentation in zip(init_pits, augmentation)
)
amphibian_costs = [
    10 ** amphibian_index for amphibian_index in range(len(amphibian_types))
]

reduced_pits = []
for pit_index in range(len(init_pits)):
    pit = init_pits[pit_index]
    while len(pit) > 0 and pit[-1] == amphibian_types[pit_index]:
        pit = pit[:-1]
    reduced_pits.append(pit)
init_pits = tuple(reduced_pits)
init_state = (init_pits, init_hallway)

states = [(0, init_state)]
processed_maps = set()

while len(states) > 0:
    current_cost, current_map = heapq.heappop(states)
    if current_map in processed_maps:
        continue
    processed_maps.add(current_map)
    current_pits, current_hall = current_map
    if all([len(pit) == 0 for pit in current_pits]):
        print(current_cost)
        exit()
    for pit_index, pit_to_empty in enumerate(current_pits):
        if len(pit_to_empty) > 0:
            for depth_index in range(len(pit_to_empty)):
                if pit_to_empty[depth_index] != ".":
                    amphibian_to_move = pit_to_empty[depth_index]
                    new_pit = tuple(
                        "." if depth_index == depth_loop else pit_to_empty[depth_loop]
                        for depth_loop in range(len(pit_to_empty))
                    )
                    step_cost = amphibian_costs[
                        amphibian_types.index(amphibian_to_move)
                    ]

                    new_pits = tuple(
                        new_pit if pit_index == pit_loop else pit
                        for pit_loop, pit in enumerate(current_pits)
                    )
                    pit_column = pit_columns[pit_index]

                    for column_index in range(
                        parking_columns.index(pit_column - 1), -1, -1
                    ):
                        if current_hall[column_index] == ".":
                            new_cost = current_cost + step_cost * (
                                abs(parking_columns[column_index] - pit_column)
                                + depth_index
                                + 1
                            )
                            new_hall = tuple(
                                amphibian_to_move
                                if column_index == hall_column_loop
                                else hall_column
                                for hall_column_loop, hall_column in enumerate(
                                    current_hall
                                )
                            )
                            heapq.heappush(states, (new_cost, (new_pits, new_hall)))
                        else:
                            break

                    for column_index in range(
                        parking_columns.index(pit_column + 1), len(parking_columns)
                    ):
                        if current_hall[column_index] == ".":
                            new_cost = current_cost + step_cost * (
                                abs(parking_columns[column_index] - pit_column)
                                + depth_index
                                + 1
                            )
                            new_hall = tuple(
                                amphibian_to_move
                                if column_index == hall_column_loop
                                else hall_column
                                for hall_column_loop, hall_column in enumerate(
                                    current_hall
                                )
                            )
                            heapq.heappush(states, (new_cost, (new_pits, new_hall)))
                        else:
                            break

                    break

    for pit_index, pit_to_fill in enumerate(current_pits):
        step_cost = amphibian_costs[pit_index]
        if len(pit_to_fill) > 0:
            if pit_to_fill[-1] == ".":
                pit_column = pit_columns[pit_index]

                for column_index in range(
                    parking_columns.index(pit_column + 1), len(parking_columns)
                ):
                    if current_hall[column_index] != ".":
                        if current_hall[column_index] == amphibian_types[pit_index]:
                            new_cost = current_cost + step_cost * (
                                abs(parking_columns[column_index] - pit_column)
                                + len(pit_to_fill)
                            )
                            new_hall = tuple(
                                "." if hall_column_loop == column_index else hall_column
                                for hall_column_loop, hall_column in enumerate(
                                    current_hall
                                )
                            )
                            new_pits = tuple(
                                pit_to_fill[:-1] if pit_loop == pit_index else pit
                                for pit_loop, pit in enumerate(current_pits)
                            )
                            heapq.heappush(states, (new_cost, (new_pits, new_hall)))
                        break

                for column_index in range(
                    parking_columns.index(pit_column - 1), -1, -1
                ):
                    if current_hall[column_index] != ".":
                        if current_hall[column_index] == amphibian_types[pit_index]:
                            new_cost = current_cost + step_cost * (
                                abs(parking_columns[column_index] - pit_column)
                                + len(pit_to_fill)
                            )
                            new_hall = tuple(
                                "." if hall_column_loop == column_index else hall_column
                                for hall_column_loop, hall_column in enumerate(
                                    current_hall
                                )
                            )
                            new_pits = tuple(
                                pit_to_fill[:-1] if pit_loop == pit_index else pit
                                for pit_loop, pit in enumerate(current_pits)
                            )
                            heapq.heappush(states, (new_cost, (new_pits, new_hall)))
                        break
