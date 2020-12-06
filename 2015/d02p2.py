import fileinput

input_lines = list(fileinput.input())

total_ribbon_length = 0
for line in input_lines:
    dimensions = [int(x) for x in line.strip().split("x")]
    dimensions.sort()
    total_ribbon_length += (
        2 * (dimensions[0] + dimensions[1])
        + dimensions[0] * dimensions[1] * dimensions[2]
    )
print(total_ribbon_length)
