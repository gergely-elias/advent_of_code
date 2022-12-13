import fileinput

input_lines = list(fileinput.input())
lines_per_packetpair = 2
packetpairs = []
number_of_packetpairs = (len(input_lines) + 1) // (lines_per_packetpair + 1)

for packetpair_index in range(number_of_packetpairs):
    packetpair = [
        eval(line.strip())
        for line in input_lines[
            packetpair_index
            * (lines_per_packetpair + 1) : (packetpair_index + 1)
            * (lines_per_packetpair + 1)
            - 1
        ]
    ]
    packetpairs.append(packetpair)


def sign(x):
    return (x > 0) - (x < 0)


def compare(packet1, packet2):
    if type(packet1) == list and type(packet2) == list:
        if len(packet1) == 0 or len(packet2) == 0:
            return sign(len(packet1) - len(packet2))
        else:
            first_elements_compare = compare(packet1[0], packet2[0])
            if first_elements_compare == 0:
                return compare(packet1[1:], packet2[1:])
            else:
                return first_elements_compare
    elif type(packet1) == int and type(packet2) == int:
        return sign(packet1 - packet2)
    elif type(packet1) == int and type(packet2) == list:
        return compare([packet1], packet2)
    elif type(packet1) == list and type(packet2) == int:
        return compare(packet1, [packet2])
    else:
        raise Exception


print(
    sum(
        index + 1
        for index, (line1, line2) in enumerate(packetpairs)
        if compare(line1, line2) == -1
    )
)
