import fileinput
import collections

input_lines = list(fileinput.input())

unique_numbers_of_segments = [
    length
    for length, counter in collections.Counter(
        map(len, input_lines[0].split("|")[0].strip().split())
    ).items()
    if counter == 1
]
recognizable_digit_count = 0
for line in input_lines:
    four_digit_output = list(
        map(lambda x: "".join(sorted(x)), line.split("|")[1].strip().split())
    )
    recognizable_digit_count += sum(
        len(digit_segments) in unique_numbers_of_segments
        for digit_segments in four_digit_output
    )

print(recognizable_digit_count)
