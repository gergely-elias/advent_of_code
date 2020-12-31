import fileinput

input_lines = list(fileinput.input())
input_lines.append("4294967296-4294967296")
blocked_ranges = []
for line in input_lines:
    blocked_ranges.append(tuple(map(int, line.strip().split("-"))))
blocked_ranges = sorted(blocked_ranges)

number_of_allowed_ips = 0
while len(blocked_ranges) > 0:
    allowed_candidate = blocked_ranges.pop(0)[1] + 1
    while len(blocked_ranges) > 0 and blocked_ranges[0][1] < allowed_candidate:
        blocked_ranges.pop(0)
    if len(blocked_ranges) > 0 and blocked_ranges[0][0] > allowed_candidate:
        number_of_allowed_ips += blocked_ranges[0][0] - allowed_candidate
print(number_of_allowed_ips)
