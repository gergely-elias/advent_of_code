import fileinput

input_lines = [line.strip() for line in fileinput.input()]

points = 0
for line in input_lines:
    your_numbers, winning_numbers = map(
        lambda x: set(x.split()), line.strip().split(":")[1].split("|")
    )
    count_of_matches = len(your_numbers.intersection(winning_numbers))
    if count_of_matches > 0:
        points += 2 ** (count_of_matches - 1)
print(points)
