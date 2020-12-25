import fileinput
import re

input_lines = list(fileinput.input())

line = input_lines[0].strip()

prev_length = len(line) + 1
while prev_length != len(line):
    prev_length = len(line)
    while re.search(r'\{[^\[\{\}\]]*:"red"[^\{\[\]\}]*\}', line):
        line = re.sub(r'\{[^\[\{\}\]]*:"red"[^\{\[\]\}]*\}', ",", line)
    if re.search(r"\{([^\[\{\}\]]*)\}", line):
        line = re.sub(r"\{([^\[\{\}\]]*)\}", r",\1", line)
    while re.search(r"\[([^\[\{\}\]]*)\]", line):
        line = re.sub(r"\[([^\[\{\}\]]*)\]", r",\1", line)

line = re.sub(r'[a-z:"\[\]\{\} ]', "", line)
nums = [0 if x == "" else int(x) for x in line.split(",")]
print(sum(nums))
