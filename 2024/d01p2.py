import collections
import fileinput
import math

input_lines = list(fileinput.input())

columns = tuple(zip(*[tuple(map(int, line.split())) for line in input_lines]))
column_counters = [collections.Counter(column) for column in columns]

print(
    sum(
        value * math.prod(column_counter[value] for column_counter in column_counters)
        for value in set.intersection(
            *[set(column_counter.keys()) for column_counter in column_counters]
        )
    )
)
