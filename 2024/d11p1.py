import fileinput

input_lines = list(fileinput.input())
numbers = map(int, input_lines[0].strip().split())
blinks = 25

for blink in range(blinks):
    new_numbers = []
    for n in numbers:
        n_as_string = str(n)
        digit_count = len(n_as_string)
        if n == 0:
            new_numbers.append(1)
        elif digit_count % 2 == 0:
            new_numbers.extend(
                [
                    int(n_as_string[: digit_count // 2]),
                    int(n_as_string[digit_count // 2 :]),
                ]
            )
        else:
            new_numbers.append(2024 * n)
    numbers = new_numbers
print(len(numbers))
