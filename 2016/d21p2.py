import fileinput
import re

input_lines = list(fileinput.input())

operations = reversed([line.strip() for line in input_lines])
password = "fbgdceah"
password_length = len(password)
inverted_index_based_rotation = dict()
for index in range(password_length):
    inverted_index_based_rotation[
        (2 * index + (2 if index >= 4 else 1)) % password_length
    ] = (index + (2 if index >= 4 else 1)) % password_length

for operation in operations:
    if operation.startswith("swap"):
        if operation.startswith("swap position"):
            pos_x, pos_y = sorted(list(map(int, re.findall(r"\d+", operation))))
        elif operation.startswith("swap letter"):
            letters_to_swap = re.findall(r"letter\ (\w)", operation)
            pos_x, pos_y = sorted(
                [password.index(letter) for letter in letters_to_swap]
            )
        password = (
            password[:pos_x]
            + password[pos_y]
            + password[pos_x + 1 : pos_y]
            + password[pos_x]
            + password[pos_y + 1 :]
        )
    elif operation.startswith("rotate"):
        if operation.startswith("rotate left"):
            rotation = -int(re.findall(r"\d+", operation)[0]) % password_length
        elif operation.startswith("rotate right"):
            rotation = int(re.findall(r"\d+", operation)[0])
        elif operation.startswith("rotate based"):
            letter = re.findall(r"letter\ (\w)", operation)[0]
            letter_index = password.index(letter)
            rotation = inverted_index_based_rotation[letter_index]
        password = password[rotation:] + password[:rotation]
    elif operation.startswith("reverse"):
        pos_x, pos_y = sorted(list(map(int, re.findall(r"\d+", operation))))
        password = str(
            password[:pos_x]
            + "".join(list(password[pos_x : pos_y + 1])[::-1])
            + password[pos_y + 1 :]
        )
    elif operation.startswith("move"):
        pos_x, pos_y = list(map(int, re.findall(r"\d+", operation)))
        letter = password[pos_y]
        password = password[:pos_y] + password[pos_y + 1 :]
        password = password[:pos_x] + letter + password[pos_x:]
print(password)
