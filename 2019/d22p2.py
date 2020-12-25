import fileinput
import re

input_lines = list(fileinput.input())

shuffle_steps = []
for line in input_lines:
    nums_on_line = re.findall(r"-?\d+", line)
    shuffle_steps.append((line[0], int(nums_on_line[0]) if nums_on_line else None))

deck_size = 119315717514047
shuffle_target = 101741582076661
position = 2020


def permute(old_deck_descriptor, permutation):
    return (
        (old_deck_descriptor[0] + old_deck_descriptor[1] * permutation[0]) % deck_size,
        (old_deck_descriptor[1] * (permutation[1])) % deck_size,
    )


deck_descriptor = (0, 1)
for step_type, count in shuffle_steps:
    if step_type == "c":
        deck_descriptor = (
            (deck_descriptor[0] + deck_descriptor[1] * count) % deck_size,
            deck_descriptor[1],
        )
    elif count:
        inverse = pow(count, deck_size - 2, deck_size)
        deck_descriptor = (
            deck_descriptor[0],
            (deck_descriptor[1] * inverse) % deck_size,
        )
    else:
        deck_descriptor = (
            (deck_descriptor[0] - deck_descriptor[1]) % deck_size,
            (-deck_descriptor[1]) % deck_size,
        )

shuffle_done = 0
iteration = 1
deck_descriptor_current = (0, 1)
deck_descriptor_iteration = deck_descriptor
while shuffle_done < shuffle_target:
    if iteration & shuffle_target > 0:
        shuffle_done += iteration
        deck_descriptor_current = permute(
            deck_descriptor_current, deck_descriptor_iteration
        )
    deck_descriptor_iteration = permute(
        deck_descriptor_iteration, deck_descriptor_iteration
    )
    iteration *= 2

print((deck_descriptor_current[0] + position * deck_descriptor_current[1]) % deck_size)
