input_file = open("inputd22.txt", "r")
input_lines = input_file.readlines()

import re

shuffle_steps = []
for line in input_lines:
    nums_on_line = re.findall("-?\d+", line)
    shuffle_steps.append((line[0], int(nums_on_line[0]) if nums_on_line else None))

deck_size = 10007
card = 2019

deck_descriptor = (0, 1)
for step_type, count in reversed(shuffle_steps):
    if step_type == "c":
        deck_descriptor = (
            (deck_descriptor[0] - deck_descriptor[1] * count) % deck_size,
            deck_descriptor[1],
        )
    elif count:
        deck_descriptor = (deck_descriptor[0], (deck_descriptor[1] * count) % deck_size)
    else:
        deck_descriptor = (
            (deck_descriptor[0] - deck_descriptor[1]) % deck_size,
            (-deck_descriptor[1]) % deck_size,
        )

print((deck_descriptor[0] + card * deck_descriptor[1]) % deck_size)
