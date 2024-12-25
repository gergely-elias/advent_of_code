import fileinput

input_lines = list(fileinput.input())
line_blocks = list(
    map(lambda x: x.split("\n"), "".join(input_lines).strip().split("\n\n"))
)

block_height = len(line_blocks[0])

keys = []
locks = []
for block in line_blocks:
    heights = tuple(line.count("#") for line in list(zip(*block)))
    if block[0].startswith("#"):
        locks.append(heights)
    else:
        keys.append(heights)


def fits(key, lock):
    return max(sum(heights) for heights in zip(*(key, lock))) <= block_height


print(sum(fits(key, lock) for key in keys for lock in locks))
