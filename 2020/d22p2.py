import fileinput

input_lines = list(fileinput.input())

hands_blocks = "".join(input_lines).strip().split("\n\n")

starting_hands = [list(map(int, hand.split("\n")[1:])) for hand in hands_blocks]


def game(hands):
    seen_setups_in_game = set()
    while all([len(hand) > 0 for hand in hands]):
        setup = tuple([tuple(hand) for hand in hands])
        if setup in seen_setups_in_game:
            return (0, hands)
        else:
            seen_setups_in_game.add(setup)
        drawn_cards = [hand.pop(0) for hand in hands]
        if all(
            [len(hand) >= drawn_card for hand, drawn_card in zip(hands, drawn_cards)]
        ):
            subgame_winner = game(
                [hand[:drawn_card] for hand, drawn_card in zip(hands, drawn_cards)]
            )[0]
            hands[subgame_winner].extend(
                [drawn_cards[subgame_winner], drawn_cards[1 - subgame_winner]]
            )
        else:
            winner = 0 if drawn_cards[0] > drawn_cards[1] else 1
            hands[winner].extend([drawn_cards[winner], drawn_cards[1 - winner]])
    game_winner = 0 if len(hands[0]) > 0 else 1
    return (game_winner, hands)


game_winner, final_hands = game(starting_hands)
print(
    sum(
        [
            (index + 1) * card
            for index, card in enumerate(reversed(final_hands[game_winner]))
        ]
    )
)
