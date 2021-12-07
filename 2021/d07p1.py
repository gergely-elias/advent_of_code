import fileinput

input_lines = list(fileinput.input())

crab_positions = sorted(list(map(int, input_lines[0].split(","))))
number_of_crabs = len(crab_positions)
median_crab_position = crab_positions[(number_of_crabs - 1) // 2]

print(
    sum([abs(crab_position - median_crab_position) for crab_position in crab_positions])
)
