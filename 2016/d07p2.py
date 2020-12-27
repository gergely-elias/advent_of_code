import fileinput
import re

input_lines = list(fileinput.input())

valid_lines = 0
for line in input_lines:
    chars = list(line.strip())
    inside_brackets = False
    for i in range(len(chars) - 2):
        if chars[i] == "[" or chars[i] == "]":
            inside_brackets = not inside_brackets
        elif chars[i + 1] != "[" and chars[i + 1] != "]":
            if (
                not inside_brackets
                and chars[i] == chars[i + 2]
                and chars[i] != chars[i + 1]
            ):
                if (
                    len(
                        re.findall(
                            r"\[\w*" + chars[i + 1] + chars[i] + chars[i + 1],
                            line.strip(),
                        )
                    )
                    > 0
                ):
                    valid_lines += 1
                    break
print(valid_lines)
