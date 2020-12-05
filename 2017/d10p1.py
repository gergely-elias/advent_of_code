input_file = open("inputd10.txt", "r")
input_lines = input_file.readlines()

line = input_lines[0].strip()
n = 256

current_position = 0
number_list = range(n)
lengths = [int(x) for x in line.split(",")]
skip_size = 0

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

print(number_list[0] * number_list[1])
