import collections
import fileinput

input_lines = list(fileinput.input())

room = [line.strip() for line in input_lines]
height = len(room)
width = len(room[0])

visited_states = collections.defaultdict(bool)
energized_tiles = collections.defaultdict(bool)
prev_beam_states = [((0, -1), (0, 1))]
while len(prev_beam_states):
    current_beam_states = []
    for (prev_pos_y, prev_pos_x), (prev_dir_y, prev_dir_x) in prev_beam_states:
        curr_pos_y, curr_pos_x = prev_pos_y + prev_dir_y, prev_pos_x + prev_dir_x
        if curr_pos_y in range(height) and curr_pos_x in range(width):
            tile = room[curr_pos_y][curr_pos_x]
            curr_pos = (curr_pos_y, curr_pos_x)
            if tile == ".":
                current_beam_states.append((curr_pos, (prev_dir_y, prev_dir_x)))
            elif tile == "/":
                current_beam_states.append((curr_pos, (-prev_dir_x, -prev_dir_y)))
            elif tile == "\\":
                current_beam_states.append((curr_pos, (prev_dir_x, prev_dir_y)))
            elif tile == "-":
                if prev_dir_y == 0:
                    current_beam_states.append((curr_pos, (prev_dir_y, prev_dir_x)))
                else:
                    current_beam_states.append((curr_pos, (0, 1)))
                    current_beam_states.append((curr_pos, (0, -1)))
            elif tile == "|":
                if prev_dir_x == 0:
                    current_beam_states.append((curr_pos, (prev_dir_y, prev_dir_x)))
                else:
                    current_beam_states.append((curr_pos, (1, 0)))
                    current_beam_states.append((curr_pos, (-1, 0)))
    new_beam_states = []
    for curr_pos, curr_dir in current_beam_states:
        if not visited_states[(curr_pos, curr_dir)]:
            visited_states[(curr_pos, curr_dir)] = True
            energized_tiles[curr_pos] = True
            new_beam_states.append((curr_pos, curr_dir))
    prev_beam_states = new_beam_states
print(sum(energized_tiles.values()))
