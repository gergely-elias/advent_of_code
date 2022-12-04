import fileinput
import re

input_lines = list(fileinput.input())

number_of_overlapping_pairs = 0
for line in input_lines:
    first_elf_start, first_elf_end, second_elf_start, second_elf_end = [
        int(x) for x in re.findall(r"\d+", line.strip())
    ]
    if not (first_elf_start > second_elf_end or second_elf_start > first_elf_end):
        number_of_overlapping_pairs += 1
print(number_of_overlapping_pairs)
