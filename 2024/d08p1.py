import collections
import fileinput
import itertools

input_lines = list(fileinput.input())

area = [line.strip() for line in input_lines]
height = len(area)
width = len(area[0])

antennae_by_frequency = collections.defaultdict(list)
for y in range(height):
    for x in range(width):
        if area[y][x] != ".":
            antennae_by_frequency[area[y][x]].append((y, x))


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
for frequency in antennae_by_frequency:
    for antenna_pair in itertools.combinations(antennae_by_frequency[frequency], 2):
        for antinode_position_candidate in [
            linear_combination(antenna_pair, coefficients)
            for coefficients in [(2, -1), (-1, 2)]
        ]:
            if antinode_position_candidate[0] in range(
                height
            ) and antinode_position_candidate[1] in range(width):
                antinode_positions.add(antinode_position_candidate)
print(len(antinode_positions))
