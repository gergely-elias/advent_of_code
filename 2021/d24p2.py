import fileinput
import collections

input_lines = list(fileinput.input())
program_length = len(input_lines)
number_of_digits = 14
block_length = program_length // number_of_digits

digit_process_parameters = []
for block_index in range(number_of_digits):
    block_lines = [
        line.strip()
        for line in input_lines[
            block_index * block_length : (block_index + 1) * block_length
        ]
    ]
    assert block_lines[0] == "inp w"
    assert block_lines[1] == "mul x 0"
    assert block_lines[2] == "add x z"
    assert block_lines[3] == "mod x 26"
    assert block_lines[4][:6] == "div z "
    assert block_lines[5][:6] == "add x "
    assert block_lines[6] == "eql x w"
    assert block_lines[7] == "eql x 0"
    assert block_lines[8] == "mul y 0"
    assert block_lines[9] == "add y 25"
    assert block_lines[10] == "mul y x"
    assert block_lines[11] == "add y 1"
    assert block_lines[12] == "mul z y"
    assert block_lines[13] == "mul y 0"
    assert block_lines[14] == "add y w"
    assert block_lines[15][:6] == "add y "
    assert block_lines[16] == "mul y x"
    assert block_lines[17] == "add z y"
    digit_process_parameters.append(
        (int(block_lines[4][6:]), int(block_lines[5][6:]), int(block_lines[15][6:]))
    )

assert collections.Counter(
    parameters[0] for parameters in digit_process_parameters
) == {1: number_of_digits // 2, 26: number_of_digits // 2}
assert all(
    parameters[1] > 9 for parameters in digit_process_parameters if parameters[0] == 1
)
digit_stack = []
digit_pairs_difference = []
for digit_index, digit_params in enumerate(digit_process_parameters):
    if digit_params[0] == 1:
        digit_stack.append((digit_index, digit_params[2]))
    else:
        pair_digit_index, pair_digit_param = digit_stack.pop()
        digit_pairs_difference.append(
            (pair_digit_index, digit_index, pair_digit_param + digit_params[1])
        )

output = [0] * number_of_digits
for digit_open, digit_close, difference in digit_pairs_difference:
    if difference > 0:
        output[digit_open] = 1
        output[digit_close] = 1 + difference
    else:
        output[digit_open] = 1 - difference
        output[digit_close] = 1
print("".join(map(str, output)))
