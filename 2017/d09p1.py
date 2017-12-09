input_file = open('inputd09.txt','r')
input_lines = input_file.readlines()

import re

line = input_lines[0].strip()

ignore_regexp = '!.'
garbage_regexp = '<[^>]*>'

line = re.sub(ignore_regexp, '', line)
line = re.sub(garbage_regexp, '', line)

total_score = 0
depth = 0
for char in line:
  if char == '{':
    depth +=1
    total_score += depth
  if char == '}':
    depth -=1

print total_score
