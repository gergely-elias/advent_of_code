import fileinput
import re
import itertools
import copy
import math

input_lines = list(fileinput.input())

number_of_planets = len(input_lines)
positions = []
velocities = []

for line_index in range(number_of_planets):
    positions.append(list(map(int, re.findall(r"-?\d+", input_lines[line_index]))))
dimensions = len(positions[0])
for planet_index in range(number_of_planets):
    velocities.append([0] * dimensions)

orig_positions = copy.deepcopy(positions)
orig_velocities = copy.deepcopy(velocities)


def compare(a, b):
    return (a > b) - (a < b)


iteration = 0
coord_period = [None] * dimensions
while not all(coord_period):
    iteration += 1
    coord_periods_to_find = [
        coord_index
        for coord_index in range(dimensions)
        if not coord_period[coord_index]
    ]
    for i, j in itertools.combinations(range(number_of_planets), 2):
        for coord_index in coord_periods_to_find:
            sign_of_difference = compare(
                positions[i][coord_index], positions[j][coord_index]
            )
            velocities[i][coord_index] -= sign_of_difference
            velocities[j][coord_index] += sign_of_difference

    for planet_index in range(number_of_planets):
        for coord_index in coord_periods_to_find:
            positions[planet_index][coord_index] += velocities[planet_index][
                coord_index
            ]

    for coord_index in coord_periods_to_find:
        if all(
            [
                positions[planet_index][coord_index]
                == orig_positions[planet_index][coord_index]
                and velocities[planet_index][coord_index]
                == orig_velocities[planet_index][coord_index]
                for planet_index in range(number_of_planets)
            ]
        ):
            coord_period[coord_index] = iteration


def list_lcm(integers):
    lcm = integers.pop(0)
    while len(integers) > 0:
        term = integers.pop(0)
        lcm *= term // math.gcd(lcm, term)
    return lcm


print(list_lcm(coord_period))
