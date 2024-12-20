import fileinput

input_lines = list(fileinput.input())
towels = set(map(lambda x: x.strip(), input_lines[0].strip().split(",")))
designs = [line.strip() for line in input_lines[2:]]
total_reachable_count = 0
for design in designs:
    reachable_count = [1] + [0 for _ in range(len(design))]
    for loop_index in range(1, len(design) + 1):
        for sub_loop_index in range(loop_index):
            if design[sub_loop_index:loop_index] in towels:
                reachable_count[loop_index] += reachable_count[sub_loop_index]
    total_reachable_count += reachable_count[len(design)]

print(total_reachable_count)
