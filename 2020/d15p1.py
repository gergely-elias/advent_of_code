import fileinput

input_lines = list(fileinput.input())

numbers = list(map(int, input_lines[0].strip().split(",")))

for turn in range(len(numbers), 2020):
    if numbers.count(numbers[-1]) > 1:
        reversed_numbers = list(reversed(numbers))
        last_number = reversed_numbers.pop(0)
        numbers.append(reversed_numbers.index(last_number) + 1)
    else:
        numbers.append(0)
print(numbers[-1])
