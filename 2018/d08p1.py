import fileinput
import re

input_lines = list(fileinput.input())

tree = list(map(int, re.findall(r"\d+", input_lines[0].strip())))

index = 0
numbers_of_children = []
metadata_lengths = []
result_sum = 0


def parse():
    global index, numbers_of_children, metadata_lengths, result_sum
    numbers_of_children.append(tree[index])
    metadata_lengths.append(tree[index + 1])
    index += 2
    for child in range(numbers_of_children[-1]):
        parse()
    numbers_of_children.pop()
    result_sum += sum(tree[index : index + metadata_lengths[-1]])
    index += metadata_lengths[-1]
    metadata_lengths.pop()


parse()
print(result_sum)
