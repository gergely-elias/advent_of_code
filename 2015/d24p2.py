import fileinput
import itertools
import math

input_lines = list(fileinput.input())

package_weights = [int(line) for line in input_lines]

target_weight = sum(package_weights) // 4
possible_passenger_comparments = []
for number_of_packages in range(1, len(package_weights) // 4 + 1):
    for passenger_compartment in itertools.combinations(
        package_weights, number_of_packages
    ):
        if sum(passenger_compartment) == target_weight:
            possible_passenger_comparments.append(passenger_compartment)
    if len(possible_passenger_comparments) > 0:
        break

print(
    min(
        [
            math.prod(passenger_compartment)
            for passenger_compartment in possible_passenger_comparments
        ]
    )
)
