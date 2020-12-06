import fileinput

input_lines = list(fileinput.input())

range_start = int(input_lines[0].strip().split()[-1]) * int(
    input_lines[4].strip().split()[-1]
) - int(input_lines[5].strip().split()[-1])
range_length = -int(input_lines[7].strip().split()[-1])
range_step = -int(input_lines[-2].strip().split()[-1])

search_range = range(range_start, range_start + range_length + 1, range_step)
composite_numbers = 0
for number in search_range:
    is_prime = True
    for possible_divisor in range(2, int(number ** 0.5 + 1)):
        if number % possible_divisor == 0:
            is_prime = False
            break
    if is_prime == False:
        composite_numbers += 1
print(composite_numbers)
