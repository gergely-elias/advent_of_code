import fileinput

input_lines = list(fileinput.input())

directions = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}
rotations = {"R": 1, "L": -1}

ship = (0, 0)
waypoint = (-1, 10)

for line in input_lines:
    line = line.strip()
    action, value = line[0], int(line[1:])
    if action in directions:
        waypoint = (
            waypoint[0] + value * directions[action][0],
            waypoint[1] + value * directions[action][1],
        )
    elif action == "F":
        ship = (ship[0] + value * waypoint[0], ship[1] + value * waypoint[1])
    else:
        right_turns = value // 90 * rotations[action] % 4
        for _ in range(right_turns):
            waypoint = (waypoint[1], -waypoint[0])
print(abs(ship[0]) + abs(ship[1]))
