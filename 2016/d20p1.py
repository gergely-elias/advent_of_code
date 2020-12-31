import fileinput

input_lines = list(fileinput.input())

blocked_ranges = []
for line in input_lines:
    blocked_ranges.append(tuple(map(int, line.strip().split("-"))))
blocked_ranges = sorted(blocked_ranges)

while len(blocked_ranges) > 0:
    allowed_candidate = blocked_ranges.pop(0)[1] + 1
    while len(blocked_ranges) > 0 and blocked_ranges[0][1] < allowed_candidate:
        blocked_ranges.pop(0)
    if len(blocked_ranges) == 0 or blocked_ranges[0][0] > allowed_candidate:
        print(allowed_candidate)
        break
