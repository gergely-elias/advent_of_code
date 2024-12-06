import fileinput

input_lines = list(fileinput.input())

mapped_area = [line.strip() for line in input_lines]
height = len(mapped_area)
width = len(mapped_area[0])

obstacles = set()
visited_positions = set()
for y in range(height):
    for x in range(width):
        if mapped_area[y][x] == "#":
            obstacles.add((y, x))
        elif mapped_area[y][x] == "^":
            start_position = (y, x)
            start_direction = (-1, 0)

current_position = start_position
current_direction = start_direction
while current_position[0] in range(height) and current_position[1] in range(width):
    visited_positions.add(current_position)
    next_position_candidate = tuple(
        sum(coords) for coords in zip(current_position, current_direction)
    )
    if next_position_candidate in obstacles:
        current_direction = (current_direction[1], -current_direction[0])
    else:
        current_position = next_position_candidate
print(len(visited_positions))
