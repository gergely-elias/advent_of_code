import fileinput

input_lines = list(fileinput.input())

sum_of_outputs = 0
for line in input_lines:
    signal_patterns = list(
        map(lambda x: "".join(sorted(x)), line.split("|")[0].strip().split())
    )
    four_digit_output = list(
        map(lambda x: "".join(sorted(x)), line.split("|")[1].strip().split())
    )
    number_to_segments = [None] * 10
    signal_patterns.sort(key=lambda x: len(x))
    number_to_segments[1] = signal_patterns[0]
    number_to_segments[7] = signal_patterns[1]
    number_to_segments[4] = signal_patterns[2]
    for signal_pattern in signal_patterns[3 : 5 + 1]:
        if sum([segment in signal_pattern for segment in number_to_segments[1]]) == 2:
            number_to_segments[3] = signal_pattern
        elif sum([segment in signal_pattern for segment in number_to_segments[4]]) == 3:
            number_to_segments[5] = signal_pattern
        else:
            number_to_segments[2] = signal_pattern
    for signal_pattern in signal_patterns[6 : 8 + 1]:
        if sum([segment in signal_pattern for segment in number_to_segments[4]]) == 4:
            number_to_segments[9] = signal_pattern
        elif sum([segment in signal_pattern for segment in number_to_segments[7]]) == 3:
            number_to_segments[0] = signal_pattern
        else:
            number_to_segments[6] = signal_pattern
    number_to_segments[8] = signal_patterns[9]
    output = 0
    for digit_in_output in four_digit_output:
        digit_value = number_to_segments.index(digit_in_output)
        output = output * 10 + digit_value
    sum_of_outputs += output

print(sum_of_outputs)
