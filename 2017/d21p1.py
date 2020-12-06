import fileinput
import re

input_lines = list(fileinput.input())


def segment(image, tile_size):
    return [
        [
            [image[k][j : j + tile_size] for k in range(i, i + tile_size)]
            for j in range(0, len(image), tile_size)
        ]
        for i in range(0, len(image), tile_size)
    ]


def merge(tiled_image):
    return [
        "".join(
            [
                tiled_image[tile_row_index][tile_column_index][pixel_row_index_in_tile]
                for tile_column_index in range(len(tiled_image))
            ]
        )
        for tile_row_index in range(len(tiled_image))
        for pixel_row_index_in_tile in range(len(tiled_image[0][0]))
    ]


def transpose(tile):
    return ["".join([tile[i][j] for i in range(len(tile))]) for j in range(len(tile))]


def flip(tile):
    return list(reversed(tile))


def symmetries(tile):
    init_tile = tile[:]
    r = []
    while len(r) == 0 or tile != init_tile:
        r.append(tile)
        tile = transpose(tile)
        r.append(tile)
        tile = flip(tile)
    return r


def enhance_single_tile(tile):
    for tile_variant in symmetries(tile):
        if tuple(tile_variant) in patterns:
            return patterns[tuple(tile_variant)]


def enhance(tiled_image):
    return [
        [enhance_single_tile(tile) for tile in tile_row] for tile_row in tiled_image
    ]


patterns = {}
for line in input_lines:
    line = line.strip()
    line = re.findall("[/#\.]+", line)
    patterns[tuple(re.findall("[#\.]+", line[0]))] = re.findall("[#\.]+", line[1])

image = [".#.", "..#", "###"]
steps = 5

for i in range(steps):
    tile_size = 2 + len(image) % 2
    image = merge(enhance(segment(image, tile_size)))

print("".join(image).count("#"))
