import fileinput
import math

input_lines = list(fileinput.input())

number_of_elves = int(input_lines[0].strip())
last_three_power = int(3 ** (math.log(number_of_elves - 1, 3) // 1))
print(
    (
        2 * number_of_elves - 3 * last_three_power
        if number_of_elves > 2 * last_three_power
        else number_of_elves - last_three_power
    )
)
