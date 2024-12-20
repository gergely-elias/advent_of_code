import fileinput

input_lines = list(fileinput.input())
towels = set(map(lambda x: x.strip(), input_lines[0].strip().split(",")))
designs = [line.strip() for line in input_lines[2:]]
possible_design_count = 0
for design in designs:
    reachable = [True] + [False for _ in range(len(design))]
    for loop_index in range(1, len(design) + 1):
        for sub_loop_index in range(loop_index):
            if (
                reachable[sub_loop_index]
                and design[sub_loop_index:loop_index] in towels
            ):
                reachable[loop_index] = True
                break
    possible_design_count += reachable[len(design)]

print(possible_design_count)
