import fileinput

input_lines = [line.strip() for line in fileinput.input()]

card_count = [1 for card_index in range(len(input_lines))]
for card_index, line in enumerate(input_lines):
    your_numbers, winning_numbers = map(
        lambda x: set(x.split()), line.strip().split(":")[1].split("|")
    )
    count_of_matches = len(your_numbers.intersection(winning_numbers))
    for copied_card in range(card_index + 1, card_index + count_of_matches + 1):
        card_count[copied_card] += card_count[card_index]
print(sum(card_count))
