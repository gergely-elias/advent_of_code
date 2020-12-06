import fileinput
import re

input_lines = list(fileinput.input())

time = 2503
dist_over_time = []
for line in input_lines:
    nums = [int(x) for x in re.findall("\d+", line.strip())]
    period = nums[1] + nums[2]
    dist = [
        (t // period * nums[1] + min(t % period, nums[1])) * nums[0]
        for t in range(1, time + 1)
    ]
    dist_over_time.append(dist)

points = len(dist_over_time) * [0]
for t in range(time):
    positions = [dist_over_time[reindeer][t] for reindeer in range(len(dist_over_time))]
    points = [
        points[reindeer] + (1 if (positions[reindeer] == max(positions)) else 0)
        for reindeer in range(len(dist_over_time))
    ]
print(max(points))
