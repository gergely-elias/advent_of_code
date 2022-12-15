import fileinput
import re

input_lines = list(fileinput.input())
y_of_interest = 2000000
excluded_x_coords = set()
for line in input_lines:
    sensor_x, sensor_y, beacon_x, beacon_y = [
        int(x) for x in re.findall(r"-?\d+", line.strip())
    ]
    sensor_beacon_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensor_interest_distance_y = abs(sensor_y - y_of_interest)
    sensor_interest_distance_x_min = max(
        0, sensor_beacon_distance - sensor_interest_distance_y
    )
    for interest_x in range(
        sensor_x - sensor_interest_distance_x_min,
        sensor_x + sensor_interest_distance_x_min,
    ):
        excluded_x_coords.add(interest_x)
print(len(excluded_x_coords))
