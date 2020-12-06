import fileinput

input_lines = list(fileinput.input())

light_status = 1000 * [0]
for i in range(1000):
    light_status[i] = 1000 * [0]

for line in input_lines:
    line = line.strip()
    if line[:7] == "turn on":
        line_rest = [x.split(",") for x in line[8:].split(" ")[0:3:2]]
        for i in range(int(line_rest[0][0]), int(line_rest[1][0]) + 1):
            for j in range(int(line_rest[0][1]), int(line_rest[1][1]) + 1):
                light_status[i][j] = 1
    elif line[:8] == "turn off":
        line_rest = [x.split(",") for x in line[9:].split(" ")[0:3:2]]
        for i in range(int(line_rest[0][0]), int(line_rest[1][0]) + 1):
            for j in range(int(line_rest[0][1]), int(line_rest[1][1]) + 1):
                light_status[i][j] = 0
    elif line[:6] == "toggle":
        line_rest = [x.split(",") for x in line[7:].split(" ")[0:3:2]]
        for i in range(int(line_rest[0][0]), int(line_rest[1][0]) + 1):
            for j in range(int(line_rest[0][1]), int(line_rest[1][1]) + 1):
                light_status[i][j] = 1 - light_status[i][j]

lights_on = 0
for i in range(1000):
    for j in range(1000):
        lights_on += light_status[i][j]
print(lights_on)
