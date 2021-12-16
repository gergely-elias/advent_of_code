import fileinput

input_lines = list(fileinput.input())

bitstream = ""
for bytechar in input_lines[0].strip():
    bitstream += ("000" + str(bin(int(bytechar, 16))[2:]))[-4:]

sum_of_versions = 0


def parse(bitstream, subpackets_left):
    global sum_of_versions
    if subpackets_left == 0:
        return bitstream
    if all([bit == "0" for bit in bitstream]):
        return ""

    next_block_length = 3
    packet_version = int(bitstream[:next_block_length], 2)
    bitstream = bitstream[next_block_length:]

    sum_of_versions += packet_version

    next_block_length = 3
    packet_type = int(bitstream[:next_block_length], 2)
    bitstream = bitstream[next_block_length:]

    if packet_type == 4:
        number_block_finished = False
        while not number_block_finished:
            next_block_length = 5
            number_group = bitstream[:next_block_length]
            bitstream = bitstream[next_block_length:]
            if number_group[0] == "0":
                number_block_finished = True
        return parse(bitstream, subpackets_left - 1)
    else:
        next_block_length = 1
        length_type = int(bitstream[:next_block_length], 2)
        bitstream = bitstream[next_block_length:]

        if length_type == 0:
            next_block_length = 15
            total_bit_length = int(bitstream[:next_block_length], 2)
            bitstream = bitstream[next_block_length:]

            subpsparse = parse(bitstream[:total_bit_length], float("inf"))
            bitstream = bitstream[total_bit_length:]
        else:
            next_block_length = 11
            number_of_subpackets = int(bitstream[:next_block_length], 2)
            bitstream = bitstream[next_block_length:]

            subpsparse = parse(bitstream, number_of_subpackets)
            bitstream = subpsparse

        return parse(bitstream, subpackets_left - 1)


parse(bitstream, float("inf"))
print(sum_of_versions)
