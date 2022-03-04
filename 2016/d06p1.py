import fileinput
import collections

input_lines = list(fileinput.input())

line_length = len(input_lines[0].strip())
message = ""
for letter_index in range(line_length):
    freq = collections.Counter([line[letter_index] for line in input_lines])
    message += freq.most_common(1)[0][0]
print(message)
