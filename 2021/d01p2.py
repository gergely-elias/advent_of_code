import fileinput

input_lines = list(fileinput.input())

depths = list(map(int, input_lines))

print(
    sum(
        [
            next_depth > prev_depth
            for next_depth, prev_depth in zip(depths[3:], depths[:-3])
        ]
    )
)
