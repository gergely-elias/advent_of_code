import fileinput
import collections

input_lines = list(fileinput.input())

map_of_tracks = collections.defaultdict(lambda: 0)

cart_direction_display = ["<", "^", ">", "v"]
direction_coord_change = [(-1, 0), (0, -1), (1, 0), (0, 1)]

cart_positions = []
cart_directions = []
cart_turn_phases = []
for row_index in range(len(input_lines)):
    row_of_map = input_lines[row_index].strip("\n")
    for column_index in range(len(row_of_map)):
        track_piece = row_of_map[column_index]
        map_of_tracks[(column_index, row_index)] = track_piece
        if track_piece in cart_direction_display:
            cart_positions.append((column_index, row_index))
            cart_directions.append(cart_direction_display.index(track_piece))
            cart_turn_phases.append(0)
            if cart_direction_display.index(track_piece) % 2 == 0:
                map_of_tracks[(column_index, row_index)] = "-"
            else:
                map_of_tracks[(column_index, row_index)] = "|"

while len(cart_positions) > 1:
    sorted_cart_positions = sorted(cart_positions)
    if cart_positions != sorted_cart_positions:
        sorted_cart_directions = []
        sorted_cart_turn_phases = []
        for unsorted_cart_position in sorted_cart_positions:
            unsorted_cart_index = cart_positions.index(unsorted_cart_position)
            sorted_cart_directions.append(cart_directions[unsorted_cart_index])
            sorted_cart_turn_phases.append(cart_turn_phases[unsorted_cart_index])
        cart_positions = sorted_cart_positions
        cart_directions = sorted_cart_directions
        cart_turn_phases = sorted_cart_turn_phases

    sorted_cart_index = 0
    while sorted_cart_index < len(cart_positions):
        cart_position = cart_positions[sorted_cart_index]
        cart_direction = cart_directions[sorted_cart_index]
        cart_turn_phase = cart_turn_phases[sorted_cart_index]
        cart_next_position = tuple(
            [
                change + pos
                for change, pos in zip(
                    direction_coord_change[cart_direction], cart_position
                )
            ]
        )

        if cart_next_position in cart_positions:
            if cart_positions.index(cart_next_position) < sorted_cart_index:
                sorted_cart_index -= 1
            for cart_to_remove in reversed(
                sorted([cart_positions.index(cart_next_position), sorted_cart_index])
            ):
                del cart_positions[cart_to_remove]
                del cart_directions[cart_to_remove]
                del cart_turn_phases[cart_to_remove]
            continue

        if map_of_tracks[cart_next_position] == "/":
            cart_direction = 3 - cart_direction
        elif map_of_tracks[cart_next_position] == "\\":
            cart_direction = (1 - cart_direction) % 4
        elif map_of_tracks[cart_next_position] == "+":
            cart_direction = (cart_direction + cart_turn_phase - 1) % 4
            cart_turn_phase = (cart_turn_phase + 1) % 3
        cart_positions[sorted_cart_index] = cart_next_position
        cart_directions[sorted_cart_index] = cart_direction
        cart_turn_phases[sorted_cart_index] = cart_turn_phase
        sorted_cart_index += 1
print(",".join(map(str, cart_positions[0])))
