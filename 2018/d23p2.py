import fileinput
import re
import z3

input_lines = list(fileinput.input())


def z3_abs(n):
    return z3.If(n >= 0, n, -n)


optimizer = z3.Optimize()
x, y, z = z3.Int("x"), z3.Int("y"), z3.Int("z")
bot_ranges = []
for line_index, line in enumerate(input_lines):
    bot_ranges.append(z3.Int("bot_range_" + str(line_index)))
    bot_x, bot_y, bot_z, bot_radius = map(int, re.findall(r"-?\d+", line.strip()))
    optimizer.add(
        bot_ranges[line_index]
        == z3.If(
            z3_abs(x - bot_x) + z3_abs(y - bot_y) + z3_abs(z - bot_z) <= bot_radius,
            1,
            0,
        )
    )

number_of_bots_in_range = z3.Int("number_of_bots_in_range")
optimizer.add(number_of_bots_in_range == sum(bot_ranges))
distance = z3.Int("distance")
optimizer.add(distance == z3_abs(x) + z3_abs(y) + z3_abs(z))
optimizer.maximize(number_of_bots_in_range)
optimizer.minimize(distance)
optimizer.check()
print(optimizer.model()[distance])
