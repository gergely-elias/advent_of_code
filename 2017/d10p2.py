import fileinput

input_lines = list(fileinput.input())

line = input_lines[0].strip()
n = 256

current_position = 0
number_list = range(n)
lengths = [ord(x) for x in line]
lengths += [17, 31, 73, 47, 23]
skip_size = 0
for round in range(64):
    for length in lengths:
        shifted_number_list = list(number_list[current_position:]) + list(
            number_list[:current_position]
        )
        part_to_reverse = shifted_number_list[:length]
        part_not_to_reverse = shifted_number_list[length:]
        part_to_reverse.reverse()
        shifted_number_list = part_to_reverse + part_not_to_reverse
        number_list = (
            shifted_number_list[n - current_position :]
            + shifted_number_list[: n - current_position]
        )

        current_position += length + skip_size
        current_position %= n
        skip_size += 1

hash_digits = []
for block_index in range(16):
    block = number_list[block_index * 16 : (block_index + 1) * 16]
    xor_result = 0
    for number in block:
        xor_result ^= number
    hash_digits.append(("0" + hex(xor_result)[2:])[-2:])
print("".join(hash_digits))
