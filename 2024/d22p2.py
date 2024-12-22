import collections
import fileinput

input_lines = list(fileinput.input())
starting_numbers = [int(line.strip()) for line in input_lines]

change_history_length = 4
secret_number_iterations = 2000


def mix_and_prune(secret_number, mix_value):
    return (secret_number ^ mix_value) % 16777216


def next_secret_number(number):
    number = mix_and_prune(number, number * 64)
    number = mix_and_prune(number, number // 32)
    number = mix_and_prune(number, number * 2048)
    return number


total_bananas = collections.defaultdict(int)
for n in starting_numbers:
    current_buyer_bananas = {}
    price = n % 10
    change_sequence = ()
    for iteration in range(secret_number_iterations):
        prev_price = price
        n = next_secret_number(n)
        price = n % 10
        change_sequence = change_sequence[-change_history_length + 1 :] + (
            price - prev_price,
        )
        if (
            change_sequence not in current_buyer_bananas
            and len(change_sequence) == change_history_length
        ):
            current_buyer_bananas[change_sequence] = price
    for change_sequence in current_buyer_bananas:
        total_bananas[change_sequence] += current_buyer_bananas[change_sequence]
print(max(total_bananas.values()))
