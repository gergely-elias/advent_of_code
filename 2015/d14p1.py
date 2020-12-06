import fileinput
import re

input_lines = list(fileinput.input())

time = 2503
max_dist = 0
for line in input_lines:
    nums = [int(x) for x in re.findall("\d+", line.strip())]
    period = nums[1] + nums[2]
    dist = (time // period * nums[1] + min(time % period, nums[1])) * nums[0]
    max_dist = max(max_dist, dist)
print(max_dist)
