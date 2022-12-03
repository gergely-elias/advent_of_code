import fileinput
import string

input_lines = list(fileinput.input())

priority_sum = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase
while len(input_lines):
    compartments = [set(input_lines.pop(0).strip()) for _ in range(3)]
    print(compartments)
    shared_items = set.intersection(*compartments)
    assert len(shared_items) == 1
    priority_sum += alphabet.index(shared_items.pop()) + 1
print(priority_sum)
