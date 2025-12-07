from collections import defaultdict
import fileinput

input_lines = list(fileinput.input())

tachyon_positions_with_timeline_count = {input_lines[0].index("S"): 1}
for t in range(1, len(input_lines)):
    line = input_lines[t].strip()
    prev_tachyon_positions = tachyon_positions_with_timeline_count
    tachyon_positions_with_timeline_count = defaultdict(int)
    for position, timeline_count in prev_tachyon_positions.items():
        if line[position] == "^":
            tachyon_positions_with_timeline_count[position - 1] += timeline_count
            tachyon_positions_with_timeline_count[position + 1] += timeline_count
        else:
            tachyon_positions_with_timeline_count[position] += timeline_count
print(sum(tachyon_positions_with_timeline_count.values()))
