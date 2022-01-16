import fileinput
import itertools
import re

input_lines = list(fileinput.input())
locations = set()
distances = dict()

for line in input_lines:
    location1, location2, distance_str = re.findall(
        r"(.*) to (.*) = (\d+)", line.strip()
    )[0]
    locations.update([location1, location2])
    distance = int(distance_str)
    distances[(location1, location2)] = distance
    distances[(location2, location1)] = distance

max_total_distance = 0
all_city_permutations = itertools.permutations(locations)
for city_order in all_city_permutations:
    current_total_distance = 0
    for city_index in range(len(city_order) - 1):
        current_total_distance += distances[
            tuple(city_order[city_index : city_index + 2])
        ]
    if current_total_distance > max_total_distance:
        max_total_distance = current_total_distance
print(max_total_distance)
