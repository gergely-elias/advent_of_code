import collections
import fileinput
import itertools

input_lines = list(fileinput.input())

area = [line.strip() for line in input_lines]
height = len(area)
width = len(area[0])

freqs = collections.defaultdict(list)
for y in range(height):
    for x in range(width):
        if area[y][x] != ".":
            freq = area[y][x]
            freqs[freq].append((y, x))


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


def tuple_scale(mytuple, factor):
    return tuple(factor * coord for coord in mytuple)


def linear_combination(tuples, coefficients):
    return tuple_sum(
        *(
            tuple_scale(mytuple, coefficient)
            for mytuple, coefficient in zip(tuples, coefficients)
        )
    )


antinode_positions = set()
for freq in freqs:
    for antenna_pair in itertools.combinations(freqs[freq], 2):
        for closer_antenna_index in range(2):
            position_difference_vector = linear_combination(
                antenna_pair,
                tuple(
                    1 if antenna_index == closer_antenna_index else -1
                    for antenna_index in range(2)
                ),
            )
            antinode_position_candidate = antenna_pair[closer_antenna_index]
            while antinode_position_candidate[0] in range(
                height
            ) and antinode_position_candidate[1] in range(width):
                antinode_positions.add(antinode_position_candidate)
                antinode_position_candidate = tuple_sum(
                    antinode_position_candidate, position_difference_vector
                )
print(len(antinode_positions))
