import fileinput
import re
import collections
import math
import numpy

input_lines = list(fileinput.input())

tile_blocks = "".join(input_lines).strip().split("\n\n")
big_image_size_in_tiles = int(math.sqrt(len(tile_blocks)))

edge_tile_indices = collections.defaultdict(lambda: [])
for tile_block in tile_blocks:
    tile_lines = [line.strip() for line in tile_block.split("\n")]
    tile_index = re.findall("\d+", tile_lines[0])[0]
    tile_matrix = numpy.array(
        [[1 if x == "#" else 0 for x in y] for y in tile_lines[1:]]
    )

    tile_edges = [
        tile_matrix[0, :],
        tile_matrix[0, :][::-1],
        tile_matrix[-1, :],
        tile_matrix[-1, :][::-1],
        tile_matrix[:, 0],
        tile_matrix[:, 0][::-1],
        tile_matrix[:, -1],
        tile_matrix[:, -1][::-1],
    ]
    for tile_edge in tile_edges:
        edge_id = "".join([str(edge_bit) for edge_bit in tile_edge])
        edge_tile_indices[edge_id].append(tile_index)

edges_count = [len(tiles_with_edge) for tiles_with_edge in edge_tile_indices.values()]
assert all([edge_count < 3 for edge_count in edges_count])
assert edges_count.count(2) == 4 * big_image_size_in_tiles * (
    big_image_size_in_tiles - 1
)
assert edges_count.count(1) == 8 * big_image_size_in_tiles

number_of_unmatched_edges = collections.Counter(
    [edge_tiles[0] for edge_tiles in edge_tile_indices.values() if len(edge_tiles) == 1]
)
print(
    math.prod(
        [
            int(tile_index)
            for tile_index, unmatched_edges_of_tile in number_of_unmatched_edges.items()
            if unmatched_edges_of_tile == 4
        ]
    )
)
