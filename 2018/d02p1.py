input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

import collections

count_2 = 0
count_3 = 0
for line in input_lines:
  chars = collections.defaultdict(lambda: 0)
  for char in list(line.strip()):
    chars[char] += 1
  if 2 in chars.values():
    count_2 += 1
  if 3 in chars.values():
    count_3 += 1
print(count_2 * count_3)
