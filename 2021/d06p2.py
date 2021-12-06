import fileinput
import collections

input_lines = list(fileinput.input())

age_list = map(int, input_lines[0].split(","))
current_day_age_counter = collections.Counter(age_list)
number_of_days = 256
reproduction_cycle_length = 7
maturity_overhead = 2

for day in range(number_of_days):
    next_day_age_counter = collections.defaultdict(lambda: 0)
    for age in current_day_age_counter.keys():
        if age == 0:
            next_day_age_counter[
                reproduction_cycle_length - 1
            ] += current_day_age_counter[age]
            next_day_age_counter[
                reproduction_cycle_length + maturity_overhead - 1
            ] += current_day_age_counter[age]
        else:
            next_day_age_counter[age - 1] += current_day_age_counter[age]
    current_day_age_counter = next_day_age_counter.copy()

print(sum(current_day_age_counter.values()))
