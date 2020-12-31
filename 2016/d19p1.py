import fileinput
import math

input_lines = list(fileinput.input())

number_of_elves = int(input_lines[0].strip())
print(1 + 2 * (number_of_elves - int(2 ** (math.log(number_of_elves, 2) // 1))))
