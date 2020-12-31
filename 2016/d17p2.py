import fileinput
import heapq
import hashlib

input_lines = list(fileinput.input())

password_stem = input_lines[0].strip()

grid_size = 4

heap_entry_id = 0
states = [(0, heap_entry_id, "")]
heap_entry_id += 1

directions = "UDLR"
longest_path = 0
while len(states) > 0:
    suffix_length, _, suffix = heapq.heappop(states)
    position_vertical = suffix.count("D") - suffix.count("U")
    position_horizontal = suffix.count("R") - suffix.count("L")
    if position_vertical not in range(grid_size) or position_horizontal not in range(
        grid_size
    ):
        continue
    elif position_vertical == grid_size - 1 and position_horizontal == grid_size - 1:
        longest_path = suffix_length
    else:
        hashresult = hashlib.md5((password_stem + suffix).encode("utf-8")).hexdigest()[
            : len(directions)
        ]
        for direction_index, direction in enumerate(directions):
            if hashresult[direction_index] > "a":
                heapq.heappush(
                    states, (suffix_length + 1, heap_entry_id, suffix + direction)
                )
                heap_entry_id += 1
print(longest_path)
