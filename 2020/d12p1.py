import fileinput

input_lines = list(fileinput.input())

directions = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}
rotations = {"R": 1, "L": -1}
direction_order = "ESWN"

ship = (0, 0, 0)

for line in input_lines:
    line = line.strip()
    action, value = line[0], int(line[1:])
    if action in directions:
        ship = (
            ship[0] + value * directions[action][0],
            ship[1] + value * directions[action][1],
            ship[2],
        )
    elif action == "F":
        ship = (
            ship[0] + value * directions[direction_order[ship[2]]][0],
            ship[1] + value * directions[direction_order[ship[2]]][1],
            ship[2],
        )
    else:
        ship = (ship[0], ship[1], (ship[2] + value // 90 * rotations[action]) % 4)
print(abs(ship[0]) + abs(ship[1]))
