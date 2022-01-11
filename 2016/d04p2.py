import fileinput
import re

input_lines = list(fileinput.input())

for line in input_lines:
    name = re.findall(r"^[\-a-z]+", line.strip())[0]
    sector_id = int(re.findall(r"\d+", line.strip())[0])
    checksum = re.findall(r"\[[a-z]{5}\]", line.strip())[0][1:6]

    decoded = "".join(
        [
            " "
            if letter == "-"
            else chr((ord(letter) - ord("a") + sector_id) % 26 + ord("a"))
            for letter in name
        ]
    )
    if decoded[:5] == "north":
        print(sector_id)
