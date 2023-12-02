import fileinput
from math import prod

input_lines = [line.strip() for line in fileinput.input()]
sum_of_powers = 0
for line_index, line in enumerate(input_lines):
    number_of_balls = {"red": 0, "green": 0, "blue": 0}
    game_header, game_data = line.split(":")
    game_index = int(game_header.split()[1])
    games = game_data.split(";")
    impossible = False
    for game in games:
        balls_by_color = {
            color_data[1]: int(color_data[0])
            for color_data in [colors_data.split() for colors_data in game.split(",")]
        }
        for color in balls_by_color:
            if balls_by_color[color] > number_of_balls[color]:
                number_of_balls[color] = balls_by_color[color]
    sum_of_powers += prod(number_of_balls.values())
print(sum_of_powers)
