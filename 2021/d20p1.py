import fileinput
import collections
import itertools

input_lines = list(fileinput.input())
algorithm = [1 if char == "#" else 0 for char in input_lines[0].strip()]
total_steps = 2

assert algorithm[0] == 0 or (algorithm[-1] == 0 and total_steps % 2 == 0)

input_image = collections.defaultdict(lambda: 0)
for line_index, line in enumerate(input_lines[2:]):
    for char_index, char in enumerate(line):
        if char == "#":
            input_image[(line_index, char_index)] = 1

current_image = input_image.copy()
for step in range(total_steps):
    xvalues, yvalues = zip(*current_image.keys())
    next_image = collections.defaultdict(lambda: (step % 2) * algorithm[0])
    for (y, x) in itertools.product(
        range(min(yvalues) - 1, max(yvalues) + 2),
        range(min(xvalues) - 1, max(xvalues) + 2),
    ):
        next_image[(y, x)] = algorithm[
            int(
                "".join(
                    [
                        str(current_image[neighborhood_coord])
                        for neighborhood_coord in itertools.product(
                            range(y - 1, y + 2), range(x - 1, x + 2)
                        )
                    ]
                ),
                2,
            )
        ]
    current_image = next_image.copy()

print(sum(current_image.values()))
