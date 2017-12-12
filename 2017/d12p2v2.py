input_file = open('inputd12.txt','r')
input_lines = input_file.readlines()

import re

groups = []

for line in input_lines:
  program_ids = set([int(x) for x in re.findall('\d+', line.strip())])
  for i,group in enumerate(groups):
    if len(program_ids.intersection(group)) > 0:
      program_ids.update(group)
      groups.pop(i)
  groups.append(program_ids)

print len(groups)
