import fileinput
import collections
import itertools

input_lines = list(fileinput.input())

preamble_length = 25
minimal_length_of_sum = 2
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
        target = transmitted_numbers[index]
        break

current_partial_sum = 0
partial_sums = [current_partial_sum]
for index in range(len(transmitted_numbers)):
    current_partial_sum += transmitted_numbers[index]
    partial_sums.append(current_partial_sum)

for range_start, start_partial_sum in enumerate(partial_sums[:-minimal_length_of_sum]):
    for range_length, end_partial_sum in enumerate(
        partial_sums[range_start + minimal_length_of_sum :]
    ):
        if end_partial_sum - start_partial_sum == target:
            contiguous_range = transmitted_numbers[
                range_start : range_start + range_length + 1
            ]
            print(min(contiguous_range) + max(contiguous_range))
            exit()
