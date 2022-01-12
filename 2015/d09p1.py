import fileinput
import itertools

input_lines = list(fileinput.input())

number_of_locations = int((len(input_lines) * 2) ** 0.5) + 1
distances = number_of_locations * [0]
index = 0
for i in range(number_of_locations):
    distances[i] = number_of_locations * [0]

for i in range(number_of_locations - 1):
    for j in range(i + 1, number_of_locations):
        dist = int(input_lines[index].strip().split(" ")[-1])
        distances[i][j] = dist
        distances[j][i] = dist
        index += 1

min_total_distance = float("inf")
all_city_permutations = itertools.permutations(range(number_of_locations))
for city_order in all_city_permutations:
    current_total_distance = 0
    for i in range(len(city_order) - 1):
        current_total_distance += distances[city_order[i]][city_order[i + 1]]
    if current_total_distance < min_total_distance:
        min_total_distance = current_total_distance
print(min_total_distance)
