import fileinput
from itertools import combinations

input_lines = list(fileinput.input())
max_total_joltage = 0
for line in input_lines:
    bank = list(map(int, list(line.strip())))
    max_bank_joltage = 0
    for battery1, battery2 in combinations(bank, 2):
        joltage = 10 * battery1 + battery2
        max_bank_joltage = max(max_bank_joltage, joltage)
    max_total_joltage += max_bank_joltage
print(max_total_joltage)
