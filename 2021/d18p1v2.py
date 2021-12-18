import fileinput
import math

input_lines = list(fileinput.input())

snailfish_numbers = []
for line in input_lines:
    number_depth_representation = dict()
    depth_index = ()
    char_index = 0
    while char_index < len(line.strip()):
        parsed_number = ""
        while line[char_index] not in "[],":
            parsed_number += line[char_index]
            char_index += 1
        if parsed_number != "":
            number_depth_representation[depth_index] = int(parsed_number)
        char = line[char_index]
        char_index += 1
        if char == "[":
            depth_index = depth_index + (0,)
        elif char == "]":
            depth_index = depth_index[:-1]
        elif char == ",":
            depth_index = depth_index[:-1] + (depth_index[-1] + 1,)
    snailfish_numbers.append(number_depth_representation)


def explode(number):
    deep_literal_pairs = sorted(
        [
            k[:-1]
            for k in number
            if len(k) > 4 and k[-1] == 0 and k[:-1] + (1,) in number
        ]
    )
    if len(deep_literal_pairs) > 0:
        pair_parent = deep_literal_pairs[0]
        carry_left, carry_right = number.pop(pair_parent + (0,)), number.pop(
            pair_parent + (1,)
        )
        number[pair_parent] = 0
        new_keys_sorted = sorted(number.keys())
        new_key_index = new_keys_sorted.index(pair_parent)
        if new_key_index > 0:
            number[new_keys_sorted[new_key_index - 1]] += carry_left
        if new_key_index < len(new_keys_sorted) - 1:
            number[new_keys_sorted[new_key_index + 1]] += carry_right
        return number, True
    return number, False


def split(number):
    large_numbers = {k: v for (k, v) in number.items() if v >= 10}
    reducable = len(large_numbers) > 0
    if reducable:
        lexico_first_large_key = sorted(large_numbers.keys())[0]
        for key_suffix in range(2):
            number[lexico_first_large_key + (key_suffix,)] = (
                number[lexico_first_large_key] + key_suffix
            ) // 2
        del number[lexico_first_large_key]
    return number, reducable


def reduce(number):
    reducable = True
    while reducable:
        while reducable:
            number, reducable = explode(number)
        number, reducable = split(number)
    return number


def add(number1, number2):
    result = {}
    for k in number1.keys():
        result[(0,) + k] = number1[k]
    for k in number2.keys():
        result[(1,) + k] = number2[k]
    return reduce(result)


def magnitude(number):
    return sum(math.prod([3 - c for c in k]) * v for k, v in number.items())


final_sum = snailfish_numbers[0]
for parsed_number in snailfish_numbers[1:]:
    final_sum = add(final_sum, parsed_number)
print(magnitude(final_sum))
