import fileinput
import collections
import re
import itertools

input_lines = list(fileinput.input())
number_of_players = len(input_lines)
starting_state = [0] * 2 * number_of_players
for line in input_lines:
    player, starting_space = map(int, re.findall(r"\d+", line.strip()))
    starting_state[number_of_players + player - 1] = starting_space

quantum_state = collections.defaultdict(lambda: 0)
quantum_state[tuple(starting_state)] = 1
current_player_index = 0
win_count = [0, 0]

number_of_rolls = 3
possible_roll_values = range(1, 4)
split_count = {0: 1}
for roll in range(number_of_rolls):
    new_split_count = collections.defaultdict(lambda: 0)
    for prev_sum, roll_value in itertools.product(split_count, possible_roll_values):
        new_split_count[prev_sum + roll_value] += split_count[prev_sum]
    split_count = new_split_count.copy()

score_to_win = 21
while sum(quantum_state.values()) > 0:
    next_quantum_state = collections.defaultdict(lambda: 0)
    for universe_state in quantum_state:
        if universe_state[(current_player_index - 1) % 2] >= score_to_win:
            win_count[(current_player_index - 1) % 2] += quantum_state[universe_state]
            continue
        for split in split_count:
            next_universe_state = list(universe_state)
            next_player_space = (
                universe_state[number_of_players + current_player_index] + split - 1
            ) % 10 + 1
            next_universe_state[
                number_of_players + current_player_index
            ] = next_player_space
            next_universe_state[current_player_index] += next_player_space
            next_quantum_state[tuple(next_universe_state)] += (
                split_count[split] * quantum_state[universe_state]
            )
    quantum_state = next_quantum_state.copy()
    current_player_index = (current_player_index + 1) % 2

print(max(win_count))
