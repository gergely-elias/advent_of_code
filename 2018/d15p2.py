import fileinput
import re
import operator

input_lines = list(fileinput.input())

health_points_at_start = 200
goblin_hit_points = 3


def setup_map():
    global world_map, creatures, num_of_goblins
    world_map = []
    creatures = []
    num_of_goblins = 0
    for line_index in range(len(input_lines)):
        world_map.append(list(input_lines[line_index].strip()))
        for tile_index in range(len(world_map[line_index])):
            if world_map[line_index][tile_index] == "G":
                creatures.append((line_index, tile_index, "G", health_points_at_start))
                num_of_goblins += 1
            elif world_map[line_index][tile_index] == "E":
                creatures.append((line_index, tile_index, "E", health_points_at_start))


def breadth_first_search(coord):
    global distances
    distance_level = 0
    current_level = [coord]
    processed = current_level[:]
    while len(current_level) > 0:
        next_level = []
        for (y, x) in current_level:
            if world_map[y][x] == "." or (y, x) == coord:
                distances[y][x] = distance_level
                for direction in directions:
                    neighbour_coord = tuple(
                        sum(coord) for coord in zip((y, x), direction)
                    )
                    if (
                        neighbour_coord[0] in range(len(world_map))
                        and neighbour_coord[1]
                        in range(len(world_map[neighbour_coord[0]]))
                        and neighbour_coord not in processed
                    ):
                        next_level.append(neighbour_coord)
                        processed.append(neighbour_coord)
        current_level = next_level
        distance_level += 1


opponent_type = {"E": "G", "G": "E"}
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def simulate_battle(elf_hit_points):
    global creatures, num_of_goblins, distances
    setup_map()
    turn = 0
    while num_of_goblins > 0:
        creatures.sort()
        creature_index = 0
        while creature_index < len(creatures):
            creature_on_turn = creatures[creature_index]
            all_opponents = list(
                filter(
                    lambda creature: creature[2] == opponent_type[creature_on_turn[2]],
                    creatures,
                )
            )

            squares_next_to_opponents = set(
                [
                    tuple([sum(coord) for coord in zip(opponent[:2], direction)])
                    for opponent in all_opponents
                    for direction in directions
                ]
            )
            open_squares = list(
                filter(
                    lambda square: world_map[square[0]][square[1]] == ".",
                    squares_next_to_opponents,
                )
            )
            if tuple(creature_on_turn[:2]) in squares_next_to_opponents:
                open_squares.append(tuple(creature_on_turn[:2]))
            open_squares.sort(key=operator.itemgetter(*range(2)))

            distances = [
                [float("inf")] * len(world_map[map_row_index])
                for map_row_index in range(len(world_map))
            ]
            breadth_first_search(tuple(creature_on_turn[:2]))

            open_square_distances = [
                distances[square[0]][square[1]] for square in open_squares
            ]
            minimal_open_square_distance = min(open_square_distances + [float("inf")])
            if (
                minimal_open_square_distance > 0
                and minimal_open_square_distance < float("inf")
            ):
                move_target_square = open_squares[
                    open_square_distances.index(minimal_open_square_distance)
                ]

                backward_path_from_target = [move_target_square]
                decreasing_distance_loop = minimal_open_square_distance
                while decreasing_distance_loop > 0:
                    decreasing_distance_loop -= 1
                    for direction in directions:
                        possible_next_on_path = tuple(
                            sum(coord)
                            for coord in zip(backward_path_from_target[-1], direction)
                        )
                        if (
                            distances[possible_next_on_path[0]][
                                possible_next_on_path[1]
                            ]
                            == decreasing_distance_loop
                        ):
                            backward_path_from_target.append(possible_next_on_path)
                            break
                world_map[backward_path_from_target[-1][0]][
                    backward_path_from_target[-1][1]
                ] = "."
                world_map[backward_path_from_target[-2][0]][
                    backward_path_from_target[-2][1]
                ] = creatures[creature_index][2]
                creature_on_turn = (
                    backward_path_from_target[-2][0],
                    backward_path_from_target[-2][1],
                    creatures[creature_index][2],
                    creatures[creature_index][3],
                )
                creatures[creature_index] = creature_on_turn

            attackable_opponents = list(
                filter(
                    lambda opponent: sum(
                        [
                            abs(coord1 - coord2)
                            for coord1, coord2 in zip(
                                opponent[:2], creature_on_turn[:2]
                            )
                        ]
                    )
                    == 1,
                    all_opponents,
                )
            )
            if len(attackable_opponents):
                minimal_hp = min([opponent[3] for opponent in attackable_opponents])
                weakest_attackable_opponents = list(
                    filter(
                        lambda opponent: opponent[3] == minimal_hp, attackable_opponents
                    )
                )
                weakest_attackable_opponents.sort(key=operator.itemgetter(*range(2)))
                opponent_to_attack = weakest_attackable_opponents[0]
                opponents_creature_index = creatures.index(opponent_to_attack)
                if opponent_to_attack[2] == "G":
                    reduced_health_points = opponent_to_attack[3] - elf_hit_points
                else:
                    reduced_health_points = opponent_to_attack[3] - goblin_hit_points
                if reduced_health_points > 0:
                    creatures[opponents_creature_index] = (
                        opponent_to_attack[0],
                        opponent_to_attack[1],
                        opponent_to_attack[2],
                        reduced_health_points,
                    )
                else:
                    world_map[opponent_to_attack[0]][opponent_to_attack[1]] = "."
                    del creatures[opponents_creature_index]
                    if opponent_to_attack[2] == "G":
                        num_of_goblins -= 1
                    else:
                        return -1, "G"
                    if opponents_creature_index < creature_index:
                        creature_index -= 1
                    if creature_index < len(creatures) - 1 and num_of_goblins == 0:
                        return turn * sum([creature[3] for creature in creatures]), "E"
            creature_index += 1
        turn += 1
    return turn * sum([creature[3] for creature in creatures]), "E"


elf_hit_point_thresholds = sorted(
    list(
        filter(
            lambda hit_point: hit_point > 3,
            set(
                [
                    (health_points_at_start - 1) // num_of_hits_to_kill + 1
                    for num_of_hits_to_kill in range(1, health_points_at_start + 1)
                ]
            ),
        )
    )
)

for elf_hit_point in elf_hit_point_thresholds:
    battle_result = simulate_battle(elf_hit_point)
    if battle_result[1] == "E":
        print(battle_result[0])
        break
