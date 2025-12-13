import fileinput

input_lines = list(fileinput.input())
interval_block, ingredient_block = "".join(input_lines).split("\n\n")

fresh_intervals = sorted(
    [
        tuple(map(int, line.strip().split("-")))
        for line in interval_block.strip().split("\n")
    ]
)
ingredient = [int(line.strip()) for line in ingredient_block.strip().split("\n")]

merged_fresh_intervals = [fresh_intervals[0]]
number_of_fresh_ingredients = fresh_intervals[0][1] - fresh_intervals[0][0] + 1
for interval_start, interval_end in fresh_intervals[1:]:
    if interval_start <= merged_fresh_intervals[-1][1] + 1:
        if interval_end > merged_fresh_intervals[-1][1]:
            number_of_fresh_ingredients += interval_end - merged_fresh_intervals[-1][1]
            merged_fresh_intervals[-1] = (merged_fresh_intervals[-1][0], interval_end)
    else:
        number_of_fresh_ingredients += interval_end - interval_start + 1
        merged_fresh_intervals.append((interval_start, interval_end))
print(number_of_fresh_ingredients)
