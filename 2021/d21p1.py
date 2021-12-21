import fileinput
import re

input_lines = list(fileinput.input())
number_of_players = 2
player_spaces = [0] * number_of_players
for line in input_lines:
    player, starting_space = map(int, re.findall(r"\d+", line.strip()))
    player_spaces[player - 1] = starting_space

scores = [0] * number_of_players
current_player_index = 0
number_of_rolls = 3
score_to_win = 1000
total_rolls = 0

while scores[1 - current_player_index] < score_to_win:
    for roll in range(number_of_rolls):
        total_rolls += 1
        player_spaces[current_player_index] += total_rolls % 100
        player_spaces[current_player_index] = (
            player_spaces[current_player_index] - 1
        ) % 10 + 1
    scores[current_player_index] += player_spaces[current_player_index]
    current_player_index = 1 - current_player_index

print(scores[current_player_index] * total_rolls)
