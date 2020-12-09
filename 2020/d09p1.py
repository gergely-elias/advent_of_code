import fileinput
import itertools

input_lines = list(fileinput.input())

preamble_length = 25
transmitted_numbers = [int(line.strip()) for line in input_lines]

for index in range(preamble_length, len(transmitted_numbers)):
    pair_sums = set(
        [
            sum(pair)
            for pair in itertools.combinations(
                transmitted_numbers[index - preamble_length : index], 2
            )
        ]
    )
    if transmitted_numbers[index] not in pair_sums:
        print(transmitted_numbers[index])
        exit()
