import fileinput
import collections
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

neighbour_directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != y]
for step in range(100):
    flipped_neighbours = collections.defaultdict(lambda: 0)
    next_step_flipped_tiles = set()
    for x, y in flipped_tiles:
        for neighbour_offset_x, neighbour_offset_y in neighbour_directions:
            flipped_neighbours[(x + neighbour_offset_x, y + neighbour_offset_y)] += 1
    for tile in flipped_neighbours:
        if (tile in flipped_tiles and 1 <= flipped_neighbours[tile] <= 2) or (
            tile not in flipped_tiles and flipped_neighbours[tile] == 2
        ):
            next_step_flipped_tiles.add(tile)
    flipped_tiles = next_step_flipped_tiles.copy()
print(len(next_step_flipped_tiles))
