import fileinput

input_lines = list(fileinput.input())

hands_blocks = "".join(input_lines).strip().split("\n\n")

hands = [list(map(int, hand.split("\n")[1:])) for hand in hands_blocks]

while all([len(hand) > 0 for hand in hands]):
    drawn_cards = [hand.pop(0) for hand in hands]
    winner = 0 if drawn_cards[0] > drawn_cards[1] else 1
    hands[winner].extend([drawn_cards[winner], drawn_cards[1 - winner]])

game_winner = 0 if len(hands[0]) > 0 else 1
print(
    sum([(index + 1) * card for index, card in enumerate(reversed(hands[game_winner]))])
)
