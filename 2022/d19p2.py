import fileinput
import re
import collections
import copy

input_lines = list(fileinput.input())
blueprints = []
for line in input_lines:
    assert re.match(
        r"Blueprint \d+: "
        r"Each ore robot costs \d+ ore. "
        r"Each clay robot costs \d+ ore. "
        r"Each obsidian robot costs \d+ ore and \d+ clay. "
        r"Each geode robot costs \d+ ore and \d+ obsidian.",
        line,
    )
    integers_on_line = [int(x) for x in re.findall(r"\d+", line.strip())]
    blueprints.append(
        (
            integers_on_line[0],
            (
                (integers_on_line[1], 0, 0, 0),
                (integers_on_line[2], 0, 0, 0),
                (integers_on_line[3], integers_on_line[4], 0, 0),
                (integers_on_line[5], 0, integers_on_line[6], 0),
            ),
        )
    )


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


def tuple_diff(minuend, subtrahend):
    return tuple(
        minuend_coord - subtrahend_coord
        for minuend_coord, subtrahend_coord in zip(minuend, subtrahend)
    )


def all_coords_greater_or_equal(tuple1, tuple2):
    return all(coord1 >= coord2 for coord1, coord2 in zip(tuple1, tuple2))


def robots_and_stones_after_new_robot(stones, robots, new_robot_index, robot_price):
    next_robots = tuple(
        robot_amount + (1 if robot_index == new_robot_index else 0)
        for robot_index, robot_amount in enumerate(robots)
    )
    next_stones = tuple_sum(tuple_diff(stones, robot_price), robots)
    return next_robots, next_stones


def determine_next_states(robot_prices, robots_available, stones_available):
    next_configs = []
    if all_coords_greater_or_equal(stones_available, robot_prices[3]):
        next_robots, next_stones = robots_and_stones_after_new_robot(
            stones_available, robots_available, 3, robot_prices[3]
        )
        next_configs.append((next_robots, next_stones))
    elif all_coords_greater_or_equal(stones_available, robot_prices[2]):
        next_robots, next_stones = robots_and_stones_after_new_robot(
            stones_available, robots_available, 2, robot_prices[2]
        )
        next_configs.append((next_robots, next_stones))
    else:
        if all_coords_greater_or_equal(stones_available, robot_prices[1]):
            next_robots, next_stones = robots_and_stones_after_new_robot(
                stones_available, robots_available, 1, robot_prices[1]
            )
            next_configs.append((next_robots, next_stones))
        if all_coords_greater_or_equal(stones_available, robot_prices[0]):
            next_robots, next_stones = robots_and_stones_after_new_robot(
                stones_available, robots_available, 0, robot_prices[0]
            )
            next_configs.append((next_robots, next_stones))
        next_robots, next_stones = robots_available, tuple_sum(
            stones_available, robots_available
        )
        next_configs.append((next_robots, next_stones))
    return next_configs


def update_optimals(previous_optimals, candidate):
    if candidate in previous_optimals:
        return previous_optimals

    for previous_optimal in previous_optimals:
        if all_coords_greater_or_equal(previous_optimal, candidate):
            return previous_optimals

    updated_optimals = [candidate]
    for previous_optimal in previous_optimals:
        if not all_coords_greater_or_equal(candidate, previous_optimal):
            updated_optimals.append(previous_optimal)
    return updated_optimals


product = 1
for blueprint_id, robot_prices in blueprints[:3]:
    start_state = (0, (1, 0, 0, 0), (0, 0, 0, 0))
    states_at_current_timestamp = {start_state}
    robot_setups_at_timestamp = collections.defaultdict(set)
    optimal_stone_setups_at_timestamp_and_robots = collections.defaultdict(list)
    total_time = 32
    for time in range(total_time):
        states_at_next_timestamp = set()
        for current_state in states_at_current_timestamp:
            timestamp, current_robots, current_stones = current_state

            next_states = determine_next_states(
                robot_prices, current_robots, current_stones
            )
            for next_robots, next_stones in next_states:
                robot_setups_at_timestamp[timestamp + 1].add(next_robots)
                optimal_stone_setups_at_timestamp_and_robots[
                    (timestamp + 1, next_robots)
                ] = update_optimals(
                    optimal_stone_setups_at_timestamp_and_robots[
                        (timestamp + 1, next_robots)
                    ],
                    next_stones,
                )

        for robot_setup in robot_setups_at_timestamp[timestamp + 1]:
            for stone_setup in optimal_stone_setups_at_timestamp_and_robots[
                (timestamp + 1, robot_setup)
            ]:
                states_at_next_timestamp.add((timestamp + 1, robot_setup, stone_setup))
        states_at_current_timestamp = copy.deepcopy(states_at_next_timestamp)
    product *= max(final_state[2][3] for final_state in states_at_current_timestamp)
print(product)
