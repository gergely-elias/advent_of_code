input_file = open('inputd09.txt','r')
input_lines = input_file.readlines()

import re

line = input_lines[0].strip()

ignore_regexp = '!.'
garbage_regexp = '<[^>]*>'

line = re.sub(ignore_regexp, '', line)
length_with_garbage = len(line)
number_of_garbages = len(re.findall(garbage_regexp, line))
line = re.sub(garbage_regexp, '', line)
length_without_garbage = len(line)

print length_with_garbage - length_without_garbage - 2 * number_of_garbages
