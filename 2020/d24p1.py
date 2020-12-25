import fileinput
import re

input_lines = list(fileinput.input())
flipped_tiles = set()
possible_directions = ["e", "w", "nw", "se", "sw", "ne"]
for line in input_lines:
    tile_path = re.findall(r"[ns]?[we]", line.strip())
    cube_coordinate = [0, 0, 0]
    for direction in tile_path:
        direction_index = possible_directions.index(direction)
        cube_coordinate[direction_index // 2] += -1 if direction_index % 2 else 1
        cube_coordinate[(direction_index // 2 + 2) % 3] += (
            1 if direction_index % 2 else -1
        )
    flipped_tiles ^= {tuple(cube_coordinate[:2])}
print(len(flipped_tiles))
