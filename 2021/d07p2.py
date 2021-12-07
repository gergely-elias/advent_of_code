import fileinput

input_lines = list(fileinput.input())

crab_positions = list(map(int, input_lines[0].split(",")))

optimal_fuel_consumption = float("inf")
for possible_optimal_position in range(min(crab_positions), max(crab_positions)):
    fuel_consumption = sum(
        [
            abs(crab_position - possible_optimal_position)
            * (abs(crab_position - possible_optimal_position) + 1)
            // 2
            for crab_position in crab_positions
        ]
    )
    if fuel_consumption < optimal_fuel_consumption:
        optimal_fuel_consumption = fuel_consumption

print(optimal_fuel_consumption)
