import fileinput

input_lines = list(fileinput.input())

tiles = input_lines[0].strip().replace("^", "1").replace(".", "0")
row_length = len(tiles)

iterations = 40
total_count_safe_tiles = 0
for iteration in range(iterations):
    count_safe_tiles = row_length - tiles.count("1")
    total_count_safe_tiles += count_safe_tiles
    tiles_decimal = int(tiles, 2)
    next_tiles_decimal = ((tiles_decimal ^ (tiles_decimal << 2)) >> 1) & (
        2 ** row_length - 1
    )
    tiles = bin(next_tiles_decimal)[2:]
print(total_count_safe_tiles)
