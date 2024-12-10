import fileinput
import networkx

input_lines = list(fileinput.input())
height_map = [list(map(int, list(line.strip()))) for line in input_lines]
height = len(height_map)
width = len(height_map[0])

steps = networkx.DiGraph()
lows = []
highs = []
for y in range(height):
    for x in range(width):
        if y > 0 and height_map[y][x] + 1 == height_map[y - 1][x]:
            steps.add_edge((y, x), (y - 1, x))
        if x > 0 and height_map[y][x] + 1 == height_map[y][x - 1]:
            steps.add_edge((y, x), (y, x - 1))
        if y < height - 1 and height_map[y][x] + 1 == height_map[y + 1][x]:
            steps.add_edge((y, x), (y + 1, x))
        if x < width - 1 and height_map[y][x] + 1 == height_map[y][x + 1]:
            steps.add_edge((y, x), (y, x + 1))
for y in range(height):
    for x in range(width):
        if height_map[y][x] == 0 and (y, x) in steps.nodes:
            lows.append((y, x))
        if height_map[y][x] == 9 and (y, x) in steps.nodes:
            highs.append((y, x))

score_sum = 0
for low in lows:
    for high in highs:
        if networkx.has_path(steps, low, high):
            score_sum += 1
print(score_sum)
