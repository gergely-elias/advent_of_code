import fileinput

input_lines = list(fileinput.input())

tachyon_positions = [input_lines[0].index("S")]
split_count = 0
for time in range(1, len(input_lines)):
    line = input_lines[time].strip()
    prev_tachyon_positions = tachyon_positions
    tachyon_positions = set()
    for position in prev_tachyon_positions:
        if line[position] == "^":
            tachyon_positions.update({position - 1, position + 1})
            split_count += 1
        else:
            tachyon_positions.update({position})
    tachyon_positions = list(tachyon_positions)
print(split_count)
