import fileinput

input_lines = list(fileinput.input())
heights = [list(map(int, list(line.strip()))) for line in input_lines]

sum_of_risk_levels = 0
for y in range(len(heights)):
    for x in range(len(heights[0])):
        if (
            (x == 0 or heights[y][x] < heights[y][x - 1])
            and (x == len(heights[0]) - 1 or (heights[y][x] < heights[y][x + 1]))
            and (y == 0 or heights[y][x] < heights[y - 1][x])
            and (y == len(heights) - 1 or heights[y][x] < heights[y + 1][x])
        ):
            sum_of_risk_levels += heights[y][x] + 1

print(sum_of_risk_levels)
