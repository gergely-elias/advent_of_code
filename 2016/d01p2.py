import fileinput

input_lines = list(fileinput.input())

path = [x.strip() for x in input_lines[0].split(",")]

position = [0, 0]
direction = 0
visited_positions = [position[:]]

for step in path:
    turn = step[0]
    length = int(step[1:])
    direction = (direction + (1 if turn == "R" else -1)) % 4
    for unit_step in range(length):
        position[direction % 2] += 1 - (direction // 2) * 2
        if position in visited_positions:
            print(sum(abs(i) for i in position))
            exit()
        else:
            visited_positions.append(position[:])
