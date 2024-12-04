import fileinput
import itertools

input_lines = list(fileinput.input())

grid = [line.strip() for line in input_lines]
height = len(grid)
width = len(grid[0])
target_word = "MAS"
directions = set(itertools.product([-1, 1], repeat=2))

count = 0
for center_y in range(1, height - 1):
    for center_x in range(1, width - 1):
        center_count = 0
        for direction_y, direction_x in directions:
            if (
                "".join(
                    grid[center_y + direction_y * (letter_index - 1)][
                        center_x + direction_x * (letter_index - 1)
                    ]
                    for letter_index in range(len(target_word))
                )
                == target_word
            ):
                center_count += 1
        if center_count == 2:
            count += 1
print(count)
