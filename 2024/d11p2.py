import collections
import fileinput

input_lines = list(fileinput.input())
numbers = map(int, input_lines[0].strip().split())
blinks = 75

number_tally = collections.Counter(numbers)
mapping = {0: [1]}
for blink in range(blinks):
    new_number_tally = collections.defaultdict(int)
    for n in number_tally:
        if n not in mapping:
            n_as_string = str(n)
            digits = len(n_as_string)
            if digits % 2 == 0:
                mapping[n] = [
                    int(n_as_string[: digits // 2]),
                    int(n_as_string[digits // 2 :]),
                ]
            else:
                mapping[n] = [2024 * n]
        for mapped_n in mapping[n]:
            new_number_tally[mapped_n] += number_tally[n]
            new_number_tally[mapped_n] %= 10**25 + 7
    number_tally = new_number_tally
print(sum(number_tally.values()))
