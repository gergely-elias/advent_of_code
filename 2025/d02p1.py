import fileinput

input_lines = list(fileinput.input())
intervals = input_lines[0].strip().split(",")

REPEAT_COUNT = 2
sum_of_invalid_ids = 0
for interval in intervals:
    a, b = map(int, interval.split("-"))
    min_repeated_pattern_length, max_repeated_pattern_length = (
        len(str(a)) + 1
    ) // REPEAT_COUNT, (len(str(b)) + 1) // REPEAT_COUNT
    for repeated_pattern_length in range(
        min_repeated_pattern_length, max_repeated_pattern_length + 1
    ):
        for possible_repeated_pattern in range(
            10 ** (repeated_pattern_length - 1), 10**repeated_pattern_length
        ):
            invalid_id = int(REPEAT_COUNT * str(possible_repeated_pattern))
            if a <= invalid_id <= b:
                sum_of_invalid_ids += invalid_id
print(sum_of_invalid_ids)
