import fileinput

input_lines = list(fileinput.input())

divisor_sum_threshold = int(input_lines[0]) // 11
candidate = 1
while (
    sum(
        [0 if candidate % divisor else candidate // divisor for divisor in range(1, 51)]
    )
    < divisor_sum_threshold
):
    candidate += 1
print(candidate)
