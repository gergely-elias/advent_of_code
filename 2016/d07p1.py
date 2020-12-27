import fileinput

input_lines = list(fileinput.input())

valid_lines = 0
for line in input_lines:
    chars = list(line.strip())
    inside_brackets = False
    abba_in = False
    abba_out = False
    for i in range(len(chars) - 3):
        if chars[i] == "[" or chars[i] == "]":
            inside_brackets = not inside_brackets
        if (
            chars[i] == chars[i + 3]
            and chars[i + 1] == chars[i + 2]
            and chars[i] != chars[i + 1]
        ):
            if inside_brackets:
                abba_in = True
                break
            else:
                abba_out = True
    if abba_out and not abba_in:
        valid_lines += 1
print(valid_lines)
