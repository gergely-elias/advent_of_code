import fileinput
import itertools
import math

input_lines = list(fileinput.input())

package_weights = [int(line) for line in input_lines]

number_of_compartments = 3
target_weight = sum(package_weights) // number_of_compartments
possible_passenger_compartments = []
for number_of_packages in range(1, len(package_weights) // number_of_compartments + 1):
    for passenger_compartment in itertools.combinations(
        package_weights, number_of_packages
    ):
        if sum(passenger_compartment) == target_weight:
            possible_passenger_compartments.append(passenger_compartment)
    if len(possible_passenger_compartments) > 0:
        break

print(
    min(
        [
            math.prod(passenger_compartment)
            for passenger_compartment in possible_passenger_compartments
        ]
    )
)
