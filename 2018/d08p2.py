input_file = open("inputd08.txt", "r")
input_lines = input_file.readlines()

import re
import sys

sys.setrecursionlimit(5000)

tree = list(map(int, re.findall("\d+", input_lines[0].strip())))

index = 0
numbers_of_children = []
metadata_lengths = []
metadata_stack = []
last_metadata_sum = 0


def parse():
    global index, numbers_of_children, metadata_lengths, metadata_stack, last_metadata_sum
    numbers_of_children.append(tree[index])
    metadata_lengths.append(tree[index + 1])
    index += 2

    for child in range(numbers_of_children[-1]):
        parse()

    if numbers_of_children[-1] == 0:
        metadata_sum = sum(tree[index : index + metadata_lengths[-1]])
    else:
        metadata_sum = 0
        for metadata_reference in [
            x - 1 for x in tree[index : index + metadata_lengths[-1]]
        ]:
            if metadata_reference < len(metadata_stack[-numbers_of_children[-1] :]):
                metadata_sum += metadata_stack[-numbers_of_children[-1] :][
                    metadata_reference
                ]
        del metadata_stack[-numbers_of_children[-1] :]
    metadata_stack.append(metadata_sum)
    index += metadata_lengths[-1]

    numbers_of_children.pop()
    metadata_lengths.pop()
    last_metadata_sum = metadata_stack[-1]


parse()
print(last_metadata_sum)
