import fileinput

input_lines = list(fileinput.input())


def is_safe(numbers):
    differences = [a - b for a, b in zip(numbers[1:], numbers[:-1])]
    return (
        (max(differences) < 0 or min(differences) > 0)
        and min(map(abs, differences)) >= 1
        and max(map(abs, differences)) <= 3
    )


safe_count = 0
for line in input_lines:
    numbers = list(map(int, line.split()))
    if is_safe(numbers):
        safe_count += 1
    else:
        numbers_copy = numbers[:]
        for i in range(len(numbers)):
            if is_safe(numbers[:i] + numbers[i + 1 :]):
                safe_count += 1
                break
print(safe_count)
