input_file = open('inputd02.txt','r')
input_lines = input_file.readlines()

count_2 = 0
count_3 = 0
for line in input_lines:
  line = list(line.strip())
  chars = {}
  for char in line:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  has_2 = False
  has_3 = False
  for i in chars:
    if chars[i] == 2:
      has_2 = True
    elif chars[i] == 3:
      has_3 = True
  if has_2:
    count_2 += 1
  if has_3:
    count_3 += 1
print count_2 * count_3
