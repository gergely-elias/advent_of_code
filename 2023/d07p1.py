import collections
import fileinput

input_lines = list(fileinput.input())

card_strength_order = "23456789TJQKA"
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
    return type_strength_order.index(tuple(sorted(collections.Counter(hand).values())))


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
