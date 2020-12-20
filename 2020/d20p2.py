import fileinput
import re
import collections
import math
import numpy

input_lines = list(fileinput.input())

tile_blocks = "".join(input_lines).strip().split("\n\n")
big_image_size_in_tiles = int(math.sqrt(len(tile_blocks)))
tile_size_with_frame = len(tile_blocks[0].split("\n")[0].strip())
tile_size = tile_size_with_frame - 2
big_image_size = big_image_size_in_tiles * tile_size
oriented_edge_tile_indices = collections.defaultdict(lambda: [])
tile_contents = dict()
for tile_block in tile_blocks:
    tile_lines = [line.strip() for line in tile_block.split("\n")]
    tile_index = re.findall("\d+", tile_lines[0])[0]
    tile_matrix = numpy.array(
        [[1 if x == "#" else 0 for x in y] for y in tile_lines[1:]]
    )

    tile_edges = {
        (0, 0): tile_matrix[0, :],
        (0, 1): tile_matrix[:, -1],
        (0, 2): tile_matrix[-1, :][::-1],
        (0, 3): tile_matrix[:, 0][::-1],
        (1, 0): tile_matrix[0, :][::-1],
        (1, 1): tile_matrix[:, 0],
        (1, 2): tile_matrix[-1, :],
        (1, 3): tile_matrix[:, -1][::-1],
    }
    for orientation, tile_edge in tile_edges.items():
        edge_id = "".join([str(edge_bit) for edge_bit in tile_edge])
        oriented_edge_tile_indices[edge_id].append(
            tile_index + str(orientation[0]) + str(orientation[1])
        )
    tile_contents[tile_index] = tile_matrix[1:-1, 1:-1]

edges_count = [
    len(tiles_with_edge) for tiles_with_edge in oriented_edge_tile_indices.values()
]
assert all([edge_count < 3 for edge_count in edges_count])
assert edges_count.count(2) == 4 * big_image_size_in_tiles * (
    big_image_size_in_tiles - 1
)
assert edges_count.count(1) == 8 * big_image_size_in_tiles

unmatched_edges = [
    edge_tiles[0]
    for edge_tiles in oriented_edge_tile_indices.values()
    if len(edge_tiles) == 1
]

edge_pairs = dict()
for edge_tiles in oriented_edge_tile_indices.values():
    if len(edge_tiles) == 2:
        edge_pairs[edge_tiles[0]] = edge_tiles[1]
        edge_pairs[edge_tiles[1]] = edge_tiles[0]

big_image_tiles = [
    [None for tile_x in range(big_image_size_in_tiles)]
    for tile_y in range(big_image_size_in_tiles)
]

for tile in unmatched_edges:
    tile_side = tile[:5]
    tile_rotation = int(tile[5])
    if tile_side + str((tile_rotation - 1) % 4) in unmatched_edges:
        big_image_tiles[0][0] = tile
        break

for tile_x in range(1, big_image_size_in_tiles):
    neighbour_tile = big_image_tiles[0][tile_x - 1]
    edge_to_match = neighbour_tile[:5] + str((int(neighbour_tile[5]) + 1) % 4)
    matching_edge = edge_pairs[edge_to_match]
    tile = (
        matching_edge[:4]
        + str((int(matching_edge[4]) + 1) % 2)
        + str((1 - int(matching_edge[5])) % 4)
    )
    big_image_tiles[0][tile_x] = tile

for tile_x in range(big_image_size_in_tiles):
    for tile_y in range(1, big_image_size_in_tiles):
        neighbour_tile = big_image_tiles[tile_y - 1][tile_x]
        edge_to_match = neighbour_tile[:5] + str((int(neighbour_tile[5]) + 2) % 4)
        matching_edge = edge_pairs[edge_to_match]
        tile = (
            matching_edge[:4]
            + str((int(matching_edge[4]) + 1) % 2)
            + str((-int(matching_edge[5])) % 4)
        )
        big_image_tiles[tile_y][tile_x] = tile


big_image = numpy.array(
    [[0 for x in range(big_image_size)] for y in range(big_image_size)]
)
for tile_y in range(big_image_size_in_tiles):
    for tile_x in range(big_image_size_in_tiles):
        tile = big_image_tiles[tile_y][tile_x]
        tile_index = tile[:4]
        tile_flip = int(tile[4])
        tile_rotation = int(tile[5])
        tile_content = tile_contents[tile_index]
        if tile_flip == 1:
            tile_content = numpy.fliplr(tile_content)
        tile_content = numpy.rot90(tile_content, tile_rotation)
        big_image[
            tile_y * tile_size : (tile_y + 1) * tile_size,
            tile_x * tile_size : (tile_x + 1) * tile_size,
        ] = tile_content

monster = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   \n"
number_of_monster_pixels = monster.count("#")
monster_matrix = numpy.array(
    [[1 if x == "#" else 0 for x in y] for y in monster.strip("\n").split("\n")]
)
monster_size_y, monster_size_x = numpy.shape(monster_matrix)

monsters_image = numpy.array(
    [[0 for x in range(big_image_size)] for y in range(big_image_size)]
)
monster_found = False
for flip in range(2):
    for rotation in range(4):
        oriented_image = big_image[:, :]
        if flip > 0:
            oriented_image = numpy.fliplr(oriented_image)
        oriented_image = numpy.rot90(oriented_image, rotation)
        for y in range(big_image_size - monster_size_y + 1):
            for x in range(big_image_size - monster_size_x + 1):
                if (
                    sum(
                        numpy.multiply(
                            oriented_image[
                                y : y + monster_size_y, x : x + monster_size_x
                            ],
                            monster_matrix,
                        ).flatten()
                    )
                    == number_of_monster_pixels
                ):
                    monsters_image[
                        y : y + monster_size_y, x : x + monster_size_x
                    ] += monster_matrix
                    monster_found = True
        if monster_found:
            oriented_image -= monsters_image
            print(sum(numpy.maximum(oriented_image.flatten(), 0)))
            exit()
