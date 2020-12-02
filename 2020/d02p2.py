input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

import re

def parse_line(line):
  fields = re.split("\W+", line)
  return {
    'indices': [int(position_index) - 1 for position_index in fields[0:2]],
    'letter': fields[2],
    'password': fields[3],
  }

fields = ['min_count', 'max_count', 'letter', 'password']
passwords_with_policies = [parse_line(line) for line in input_lines]
print(sum([sum([entry['password'][position_index] == entry['letter'] for position_index in entry['indices']]) == 1 for entry in passwords_with_policies]))
