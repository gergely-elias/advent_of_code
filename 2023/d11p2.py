import fileinput
import itertools

input_lines = list(fileinput.input())
galaxies = set()
row_expansion = [True] * len(input_lines)
column_expansion = [True] * len(input_lines[0])
for y, line in enumerate(input_lines):
    for x, char in enumerate(line.strip()):
        if char == "#":
            galaxies.add((y, x))
            row_expansion[y] = False
            column_expansion[x] = False
accumulated_taken_rows = list(
    itertools.accumulate(
        row_expansion,
        lambda partial_sum, new_expansion: partial_sum + int(new_expansion),
    )
)
accumulated_taken_cols = list(
    itertools.accumulate(
        column_expansion,
        lambda partial_sum, new_expansion: partial_sum + int(new_expansion),
    )
)

total_distance = 0
expansion_rate = 1000000
for g1, g2 in itertools.combinations(galaxies, 2):
    y1, y2 = sorted([g1[0], g2[0]])
    x1, x2 = sorted([g1[1], g2[1]])
    total_distance += (
        y2
        - y1
        + x2
        - x1
        + (expansion_rate - 1)
        * (
            accumulated_taken_rows[y2]
            - accumulated_taken_rows[y1]
            + accumulated_taken_cols[x2]
            - accumulated_taken_cols[x1]
        )
    )
print(total_distance)
