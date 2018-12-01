input_file = open('inputd10.txt','r')
input_lines = input_file.readlines()

input_num = input_lines[0].strip()

def count_digits(current_num):
  last_count = 0
  last_digit = ''
  next_num = ''
  for current_digit in current_num:
    if last_digit == '':
      last_digit = current_digit
    if current_digit == last_digit:
      last_count += 1
    else:
      next_num += str(last_count) + last_digit
      last_digit = current_digit
      last_count = 1
  next_num += str(last_count) + last_digit
  return next_num

k = input_num
for i in range(50):
  k = count_digits(k)
  print i, len(k)
