import fileinput

input_lines = list(fileinput.input())

adapters = [int(line.strip()) for line in input_lines]
adapters.sort()
joltage_differences = (
    [adapters[0]]
    + [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
    + [3]
)
print(joltage_differences.count(1) * joltage_differences.count(3))
