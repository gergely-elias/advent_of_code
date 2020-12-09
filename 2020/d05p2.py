import fileinput

input_lines = list(fileinput.input())

ids = [
    int("".join(["1" if s in "RB" else "0" for s in line.strip()]), 2)
    for line in input_lines
]
print((set(range(min(ids), max(ids) + 1)).difference(ids)).pop())
