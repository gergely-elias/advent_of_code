from collections import defaultdict
import fileinput

input_lines = list(fileinput.input())

max_total_joltage = 0
number_of_digits = 12
for line in input_lines:
    bank = list(map(int, list(line.strip())))
    maximal_prefix = defaultdict(lambda: defaultdict(int))
    for current_digit_pool_size in range(number_of_digits):
        for last_digit_index in range(
            current_digit_pool_size,
            len(bank) - number_of_digits + current_digit_pool_size + 1,
        ):
            maximal_prefix[current_digit_pool_size][last_digit_index] = max(
                10
                * maximal_prefix[current_digit_pool_size - 1][
                    possible_penultimate_digit_index
                ]
                + bank[possible_penultimate_digit_index + 1]
                for possible_penultimate_digit_index in range(
                    current_digit_pool_size - 1, last_digit_index
                )
            )
    max_bank_joltage = maximal_prefix[current_digit_pool_size][last_digit_index]
    max_total_joltage += max_bank_joltage
print(max_total_joltage)
