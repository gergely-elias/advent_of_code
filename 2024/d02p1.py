import fileinput

input_lines = list(fileinput.input())

safe_count = 0
for line in input_lines:
    numbers = list(map(int, line.split()))
    differences = [a - b for a, b in zip(numbers[1:], numbers[:-1])]
    if (
        (max(differences) < 0 or min(differences) > 0)
        and min(map(abs, differences)) >= 1
        and max(map(abs, differences)) <= 3
    ):
        safe_count += 1
print(safe_count)
