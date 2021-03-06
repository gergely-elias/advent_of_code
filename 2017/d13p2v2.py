import fileinput
import re
import collections
import math

input_lines = list(fileinput.input())

forbidden_delays = collections.defaultdict(lambda: set())

for line in input_lines:
    line = line.strip()
    line = re.findall(r"\d+", line)
    forbidden_delays[2 * (int(line[1]) - 1)].add(
        (-int(line[0])) % (2 * (int(line[1]) - 1))
    )

modulo_list = list(forbidden_delays)
modulo_list.sort()

main_modulo = 1
possible_remainders = range(1)
for current_modulo in modulo_list:
    lcm = main_modulo * current_modulo // math.gcd(main_modulo, current_modulo)
    possible_remainders_lcm = [
        x + y for x in range(0, lcm, main_modulo) for y in possible_remainders
    ]

    possible_remainders = [
        x
        for x in possible_remainders_lcm
        if x % current_modulo not in forbidden_delays[current_modulo]
    ]
    main_modulo = lcm

print(possible_remainders[0])
