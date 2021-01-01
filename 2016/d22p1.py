import fileinput
import re
import itertools

input_lines = list(fileinput.input())

nodes = [tuple(map(int, re.findall(r"\d+", line.strip()))) for line in input_lines[2:]]

print(
    len(
        [
            (node_a, node_b)
            for node_a, node_b in itertools.permutations(nodes, 2)
            if 0 < node_a[3] <= node_b[4]
        ]
    )
)
