import fileinput

input_lines = list(fileinput.input())

line_length = len(input_lines[0].strip())
message = ""
for letter_index in range(line_length):
    freq = [[0, chr(ord("a") + x)] for x in range(26)]
    for line in input_lines:
        freq[ord(list(line)[letter_index]) - ord("a")][0] += 1
    freq.sort(key=lambda x: x[0])
    message += freq[0][1]
print(message)
