import fileinput
import re

input_lines = list(fileinput.input())

id_sum = 0

for line in input_lines:
    name = re.findall(r"^[\-a-z]+", line.strip())[0]
    sector_id = int(re.findall(r"\d+", line.strip())[0])
    checksum = re.findall(r"\[[a-z]{5}\]", line.strip())[0][1:6]

    freq = [[0, chr(x + ord("a"))] for x in range(26)]
    for letter in name:
        if letter != "-":
            freq[ord(letter) - ord("a")][0] += 1
    freq = sorted(freq, key=lambda x: x[0], reverse=True)
    my_checksum = "".join([x[1] for x in freq[0:5]])
    if my_checksum == checksum:
        id_sum += sector_id
print(id_sum)
