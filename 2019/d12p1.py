import fileinput
import re
import itertools

input_lines = list(fileinput.input())

number_of_planets = len(input_lines)
positions = []
velocities = []

for line_index in range(number_of_planets):
    positions.append(list(map(int, re.findall("-?\d+", input_lines[line_index]))))
dimensions = len(positions[0])
for planet_index in range(number_of_planets):
    velocities.append([0] * dimensions)


def compare(a, b):
    return (a > b) - (a < b)


for iteration in range(1000):
    for i, j in itertools.combinations(range(number_of_planets), 2):
        for coord_index in range(dimensions):
            sign_of_difference = compare(
                positions[i][coord_index], positions[j][coord_index]
            )
            velocities[i][coord_index] -= sign_of_difference
            velocities[j][coord_index] += sign_of_difference

    for planet_index in range(number_of_planets):
        for coord_index in range(dimensions):
            positions[planet_index][coord_index] += velocities[planet_index][
                coord_index
            ]

print(
    sum(
        [
            sum([abs(coord) for coord in positions[planet_index]])
            * sum([abs(coord) for coord in velocities[planet_index]])
            for planet_index in range(number_of_planets)
        ]
    )
)
