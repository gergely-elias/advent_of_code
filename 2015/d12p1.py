input_file = open('inputd12.txt','r')
input_lines = input_file.readlines()

import re

line = input_lines[0].strip()

line = re.sub('[a-z:\"\[\]\{\}]', '', line)
nums = [0 if x == '' else int(x) for x in line.split(',')]
print(sum(nums))
