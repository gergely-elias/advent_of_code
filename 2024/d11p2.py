import collections
import fileinput

input_lines = list(fileinput.input())
numbers = map(int, input_lines[0].strip().split())
blinks = 75

number_tally = collections.Counter(numbers)
for blink in range(blinks):
    new_number_tally = collections.defaultdict(int)
    for n in number_tally:
        n_as_string = str(n)
        digits = len(n_as_string)
        if n == 0:
            new_number_tally[1] += number_tally[n]
        elif digits % 2 == 0:
            new_number_tally[int(n_as_string[: digits // 2])] += number_tally[n]
            new_number_tally[int(n_as_string[digits // 2 :])] += number_tally[n]
        else:
            new_number_tally[2024 * n] += number_tally[n]
    number_tally = new_number_tally
print(sum(number_tally.values()))
