import fileinput
import math
import sympy

input_lines = list(fileinput.input())
time = int(input_lines[0].strip().split(":")[1].replace(" ", ""))
distance = int(input_lines[1].strip().split(":")[1].replace(" ", ""))

press_time = sympy.var("x")
root1, root2 = sorted(
    sympy.solve((time / 2) ** 2 - (time / 2 - press_time) ** 2 - distance, press_time)
)
rounded_root1, rounded_root2 = math.ceil(root1), math.floor(root2)
print(rounded_root2 - rounded_root1 + 1)
