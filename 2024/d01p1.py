import fileinput

input_lines = list(fileinput.input())

columns = tuple(zip(*[tuple(map(int, line.split())) for line in input_lines]))
sorted_columns = [sorted(column) for column in columns]

print(sum(abs(a - b) for a, b in zip(*sorted_columns)))
