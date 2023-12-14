import collections
import fileinput

input_lines = list(fileinput.input())

platform_map = [line.strip() for line in input_lines]
fix_rocks = set()
rolling_rocks = set()
for y, row in enumerate(platform_map):
    for x, tile in enumerate(row):
        if tile == "#":
            fix_rocks.add((y, x))
        elif tile == "O":
            rolling_rocks.add((y, x))


def tuple_sum(*t):
    return tuple(sum(coords) for coords in zip(*t))


def tuple_opposite(t):
    return tuple(-coord for coord in t)


def roll(tilt_direction, rolling_rocks):
    support_count = collections.defaultdict(int)
    for rock in rolling_rocks:
        support = rock
        while (
            support not in fix_rocks
            and support[0] in range(len(platform_map))
            and support[1] in range(len(platform_map[0]))
        ):
            support = tuple_sum(tilt_direction, support)
        support_count[support] += 1
    rolling_rocks = set()
    for support in support_count:
        landing_position = support
        for rock in range(support_count[support]):
            landing_position = tuple_sum(
                landing_position, tuple_opposite(tilt_direction)
            )
            rolling_rocks.add(landing_position)
    return rolling_rocks


after_cycle_configurations = []
total_cycles = 1_000_000_000
for cycle_index in range(total_cycles):
    for tilt_direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        rolling_rocks = roll(tilt_direction, rolling_rocks)
    if rolling_rocks in after_cycle_configurations:
        period_start = after_cycle_configurations.index(rolling_rocks)
        rolling_rocks = after_cycle_configurations[
            period_start
            + (total_cycles - 1 - period_start) % (cycle_index - period_start)
        ]
        break
    after_cycle_configurations.append(rolling_rocks)

print(sum(len(input_lines) - rock[0] for rock in rolling_rocks))
