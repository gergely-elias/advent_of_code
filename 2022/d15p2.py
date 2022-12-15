import fileinput
import re


class PossibleIntervals:
    def __init__(self, init_intervals):
        self.intervals = init_intervals

    def exclude_interval(self, interval_to_exclude):
        exclude_a, exclude_b = interval_to_exclude
        updated_intervals = []
        for possible_a, possible_b in self.intervals:
            if exclude_a > possible_b or exclude_b < possible_a:
                updated_intervals.append((possible_a, possible_b))
            else:
                if exclude_a > possible_a:
                    updated_intervals.append((possible_a, exclude_a - 1))
                if exclude_b < possible_b:
                    updated_intervals.append((exclude_b + 1, possible_b))
        self.intervals = updated_intervals


max_coord = 4000000

input_lines = list(fileinput.input())
possible_x_intervals_by_y = {
    y: PossibleIntervals([(0, max_coord)]) for y in range(max_coord + 1)
}
for line in input_lines:
    sensor_x, sensor_y, beacon_x, beacon_y = [
        int(x) for x in re.findall(r"-?\d+", line.strip())
    ]
    sensor_beacon_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    for possible_y in possible_x_intervals_by_y:
        distress_distance_y = abs(sensor_y - possible_y)
        distress_distance_x_min = sensor_beacon_distance - distress_distance_y
        if distress_distance_x_min >= 0:
            possible_x_intervals_by_y[possible_y].exclude_interval(
                (
                    max(0, sensor_x - distress_distance_x_min),
                    min(max_coord, sensor_x + distress_distance_x_min),
                )
            )
    possible_x_intervals_by_y = {
        y: possible_x_intervals
        for y, possible_x_intervals in possible_x_intervals_by_y.items()
        if len(possible_x_intervals.intervals)
    }
assert len(possible_x_intervals_by_y) == 1
y, possible_x_intervals = list(possible_x_intervals_by_y.items())[0]
assert len(possible_x_intervals.intervals) == 1
min_x, max_x = possible_x_intervals.intervals[0]
assert min_x == max_x
print(min_x * 4000000 + y)
