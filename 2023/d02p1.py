import fileinput

input_lines = [line.strip() for line in fileinput.input()]
sum_of_possible_game_indices = 0
number_of_balls = {"red": 12, "green": 13, "blue": 14}
for line_index, line in enumerate(input_lines):
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
                impossible = True
                break
        if impossible:
            True
    if not impossible:
        sum_of_possible_game_indices += game_index
print(sum_of_possible_game_indices)
