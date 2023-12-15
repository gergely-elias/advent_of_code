import fileinput

input_lines = list(fileinput.input())
steps = input_lines[0].strip().split(",")


def hash_string(s):
    hash_value = 0
    for c in s:
        hash_value += ord(c)
        hash_value *= 17
        hash_value %= 256
    return hash_value


print(sum(hash_string(step) for step in steps))
