input_file = open('inputd07.txt','r')
input_lines = input_file.readlines()

import re
discs = re.findall('[a-z]+', ''.join(input_lines))

unique_discs = set()
for disc in discs:
  unique_discs.symmetric_difference_update(set([disc]))

print list(unique_discs)[0]

