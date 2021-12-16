import fileinput
import math

input_lines = list(fileinput.input())

bitstream = ""
for bytechar in input_lines[0].strip():
    bitstream += ("000" + str(bin(int(bytechar, 16))[2:]))[-4:]


def parse(bitstream, subpackets_left, previous_packets):
    if subpackets_left == 0:
        return (bitstream, subpackets_left, previous_packets)
    if all([bit == "0" for bit in bitstream]):
        return ("", subpackets_left, previous_packets)

    next_block_length = 3
    bitstream = bitstream[next_block_length:]

    next_block_length = 3
    packet_type = int(bitstream[0:next_block_length], 2)
    bitstream = bitstream[next_block_length:]

    if packet_type == 4:
        number_block_finished = False
        literal_bitstream = ""
        while not number_block_finished:
            next_block_length = 5
            number_group = bitstream[:next_block_length]
            bitstream = bitstream[next_block_length:]
            literal_bitstream += number_group[1:5]
            if number_group[0] == "0":
                literal_value = int(literal_bitstream, 2)
                number_block_finished = True
        return parse(bitstream, subpackets_left - 1, previous_packets + [literal_value])
    else:
        next_block_length = 1
        length_type = int(bitstream[:next_block_length], 2)
        bitstream = bitstream[next_block_length:]

        if length_type == 0:
            next_block_length = 15
            total_bit_length = int(bitstream[:next_block_length], 2)
            bitstream = bitstream[next_block_length:]

            parsed_subpacket = parse(bitstream[:total_bit_length], float("inf"), [])
            bitstream = bitstream[total_bit_length:]
        else:
            next_block_length = 11
            number_of_subpackets = int(bitstream[:next_block_length], 2)
            bitstream = bitstream[next_block_length:]

            parsed_subpacket = parse(bitstream, number_of_subpackets, [])
            bitstream = parsed_subpacket[0]

        subpacket_values = parsed_subpacket[2]
        if packet_type == 0:
            packet_value = sum(subpacket_values)
        if packet_type == 1:
            packet_value = math.prod(subpacket_values)
        if packet_type == 2:
            packet_value = min(subpacket_values)
        if packet_type == 3:
            packet_value = max(subpacket_values)
        if packet_type == 5:
            packet_value = 1 if subpacket_values[0] > subpacket_values[1] else 0
        if packet_type == 6:
            packet_value = 1 if subpacket_values[0] < subpacket_values[1] else 0
        if packet_type == 7:
            packet_value = 1 if subpacket_values[0] == subpacket_values[1] else 0

        return parse(bitstream, subpackets_left - 1, previous_packets + [packet_value])


a = parse(bitstream, float("inf"), [])
print(a[2][0])
