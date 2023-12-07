import collections
import fileinput

input_lines = list(fileinput.input())

card_strength_order = "J23456789TQKA"
type_strength_order = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2),
    (1, 2, 2),
    (1, 1, 3),
    (2, 3),
    (1, 4),
    (5,),
]


def type_of_hand(hand):
    hand_type = sorted(
        [v for card, v in collections.Counter(hand).items() if card != "J"]
    )
    number_of_jokers = hand.count("J")
    if len(hand_type):
        hand_type[-1] += number_of_jokers
    else:
        hand_type.append(number_of_jokers)
    return type_strength_order.index(tuple(hand_type))


evaluated_hands = []
for line in input_lines:
    hand = line[:5]
    bid = int(line[6:])
    evaluated_hands.append(
        (
            type_of_hand(hand),
            tuple(card_strength_order.index(card) for card in hand),
            bid,
        )
    )

print(
    sum(
        (hand_rank + 1) * hand_evaluation[-1]
        for hand_rank, hand_evaluation in enumerate(sorted(evaluated_hands))
    )
)
