import fileinput

input_lines = list(fileinput.input())

current_x = 0
current_y = 0
current_position = (current_x, current_y)
houses_visited = set()
houses_visited.add(current_position)

if len(input_lines) > 0:
    for character in input_lines[0]:
        if character == "^":
            current_y += 1
        elif character == "v":
            current_y -= 1
        elif character == ">":
            current_x += 1
        elif character == "<":
            current_x -= 1
        current_position = (current_x, current_y)
        houses_visited.add(current_position)

print(len(houses_visited))
