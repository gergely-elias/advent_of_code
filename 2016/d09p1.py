import fileinput
import re

input_lines = list(fileinput.input())

charsequence = input_lines[0].strip()
parser_offset = 0

while parser_offset < len(charsequence):
    if charsequence[parser_offset] == "(":
        marker_start = parser_offset
        marker_content = ""
        while charsequence[parser_offset + 1] != ")":
            parser_offset += 1
            marker_content += charsequence[parser_offset]
        marker_end = parser_offset + 2
        decompression_params = list(map(int, re.findall(r"\d+", marker_content)))
        charsequence = (
            charsequence[:marker_start]
            + decompression_params[1]
            * charsequence[marker_end : marker_end + decompression_params[0]]
            + charsequence[marker_end + decompression_params[0] :]
        )
        parser_offset = marker_start + decompression_params[0] * decompression_params[1]
    else:
        parser_offset += 1

print(len("".join(charsequence)))
