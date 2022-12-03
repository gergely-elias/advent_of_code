import fileinput
import string

input_lines = list(fileinput.input())

priority_sum = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase
for line in map(lambda x: x.strip(), input_lines):
    compartment_size = len(line) // 2
    compartments = set(line[:compartment_size]), set(line[compartment_size:])
    shared_items = set.intersection(*compartments)
    assert len(shared_items) == 1
    priority_sum += alphabet.index(shared_items.pop()) + 1
print(priority_sum)
