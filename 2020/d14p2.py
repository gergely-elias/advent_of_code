import fileinput
import re

input_lines = list(fileinput.input())

memory = dict()
for line in input_lines:
    line = line.strip()
    if line[:4] == "mask":
        mask = line[7:]
        ones = int(mask.replace("X", "1"), 2)
        reset = int(mask.replace("0", "1").replace("X", "0"), 2)
        mask_bit_values = [
            2 ** bit_index for bit_index, bit in enumerate(mask[::-1]) if bit == "X"
        ]
    else:
        address, value = map(int, re.findall("\d+", line))
        address = (address | ones) & reset
        for floating_submask in range(2 ** len(mask_bit_values)):
            floating_mask = sum(
                [
                    mask_bit
                    for mask_bit_index, mask_bit in enumerate(mask_bit_values)
                    if (2 ** mask_bit_index) & floating_submask > 0
                ]
            )
            memory[floating_mask | address] = value
print(sum(memory.values()))
