import fileinput
import re

input_lines = list(fileinput.input())

coordinates = [tuple(map(int, re.findall("\d+", line))) for line in input_lines]
(x_list, y_list) = map(sorted, zip(*coordinates))

num_of_coords = len(coordinates)

threshold = 10000


def partial_sums(coord_list):
    sum_at_min = sum(coord_list) - num_of_coords * coord_list[0]
    range_min = coord_list[0] - (threshold - 1 - sum_at_min) // num_of_coords

    sum_at_max = num_of_coords * coord_list[-1] - sum(coord_list)
    range_max = coord_list[-1] + (threshold - 1 - sum_at_max) // num_of_coords
    return [
        sum([abs(coord - location) for coord in coord_list])
        for location in range(range_min, range_max + 1)
    ]


x_sums = sorted(partial_sums(x_list))
y_sums = sorted(partial_sums(y_list))

x_index = 0
y_index = len(y_sums) - 1
region_size = 0
while x_index < len(x_sums) and y_index >= 0:
    if x_sums[x_index] + y_sums[y_index] < threshold:
        region_size += y_index + 1
        x_index += 1
    else:
        y_index -= 1

print(region_size)
