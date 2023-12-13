import fileinput

input_lines = list(fileinput.input())


def find_axis(island):
    for possible_axis in range(1, len(island)):
        original = list(reversed(island[:possible_axis]))
        reflection = island[possible_axis:]
        if all(seq1 == seq2 for seq1, seq2 in zip(original, reflection)):
            return True, possible_axis
    return False, None


sum_of_horizontal_axes = 0
sum_of_vertical_axes = 0
for island_raw in "".join(input_lines).split("\n\n"):
    island = island_raw.strip().split("\n")
    axis_found, horizontal_axis = find_axis(island)
    if axis_found:
        sum_of_horizontal_axes += horizontal_axis
    else:
        _, vertical_axis = find_axis(["".join(column) for column in zip(*island)])
        sum_of_vertical_axes += vertical_axis

print(100 * sum_of_horizontal_axes + sum_of_vertical_axes)
