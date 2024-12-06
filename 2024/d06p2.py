import fileinput

input_lines = list(fileinput.input())

mapped_area = [line.strip() for line in input_lines]
height = len(mapped_area)
width = len(mapped_area[0])

obstacles = set()
positions_on_original_path = set()
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
    positions_on_original_path.add(current_position)
    next_position_candidate = tuple(
        sum(coords) for coords in zip(current_position, current_direction)
    )
    if next_position_candidate in obstacles:
        current_direction = (current_direction[1], -current_direction[0])
    else:
        current_position = next_position_candidate

looping_obstacles = 0
for extra_obstacle_position in positions_on_original_path.difference({start_position}):
    previous_states = set()
    current_position = start_position
    current_direction = start_direction
    while current_position[0] in range(height) and current_position[1] in range(width):
        if (current_position, current_direction) in previous_states:
            looping_obstacles += 1
            break
        previous_states.add((current_position, current_direction))
        next_position_candidate = tuple(
            sum(coords) for coords in zip(current_position, current_direction)
        )
        if (
            next_position_candidate in obstacles
            or next_position_candidate == extra_obstacle_position
        ):
            current_direction = (current_direction[1], -current_direction[0])
        else:
            current_position = next_position_candidate
print(looping_obstacles)
