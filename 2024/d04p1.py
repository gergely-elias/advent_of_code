import fileinput
import itertools

input_lines = list(fileinput.input())

grid = [line.strip() for line in input_lines]
height = len(grid)
width = len(grid[0])
target_word = "XMAS"
directions = set(itertools.product(range(-1, 2), repeat=2))
directions.remove((0, 0))

count = 0
for direction_y, direction_x in directions:
    for start_y in range(
        max(0, -(len(target_word) - 1) * direction_y),
        height - max(0, (len(target_word) - 1) * direction_y),
    ):
        for start_x in range(
            max(0, -(len(target_word) - 1) * direction_x),
            width - max(0, (len(target_word) - 1) * direction_x),
        ):
            if (
                "".join(
                    grid[start_y + direction_y * letter_index][
                        start_x + direction_x * letter_index
                    ]
                    for letter_index in range(len(target_word))
                )
                == target_word
            ):
                count += 1
print(count)
