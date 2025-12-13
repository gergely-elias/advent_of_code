import fileinput

input_lines = list(fileinput.input())
intervals = input_lines[0].strip().split(",")

invalid_ids = set()
for interval in intervals:
    a, b = map(int, interval.split("-"))
    max_repeated_pattern_length = (len(str(b)) + 1) // 2
    for possible_repeated_pattern in range(1, 10**max_repeated_pattern_length):
        repeat_count = 2
        while repeat_count * len(str(possible_repeated_pattern)) <= len(str(b)):
            invalid_id = int(repeat_count * str(possible_repeated_pattern))
            if a <= invalid_id <= b:
                invalid_ids.add(invalid_id)
            repeat_count += 1
print(sum(invalid_ids))
