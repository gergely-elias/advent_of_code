import fileinput

input_lines = list(fileinput.input())
starting_numbers = [int(line.strip()) for line in input_lines]

secret_number_iterations = 2000


def mix_and_prune(secret_number, mix_value):
    return (secret_number ^ mix_value) % 16777216


def next_secret_number(number):
    number = mix_and_prune(number, number * 64)
    number = mix_and_prune(number, number // 32)
    number = mix_and_prune(number, number * 2048)
    return number


sum_of_final_secret_numbers = 0
for n in starting_numbers:
    for iteration in range(secret_number_iterations):
        n = next_secret_number(n)
    sum_of_final_secret_numbers += n
print(sum_of_final_secret_numbers)
