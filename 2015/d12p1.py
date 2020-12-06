import fileinput
import re

input_lines = list(fileinput.input())

line = input_lines[0].strip()

line = re.sub('[a-z:"\[\]\{\}]', "", line)
nums = [0 if x == "" else int(x) for x in line.split(",")]
print(sum(nums))
