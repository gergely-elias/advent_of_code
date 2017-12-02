input_file = open('inputd01.txt','r')
input_lines = input_file.readlines()

digit_sequence = input_lines[0].strip()
sum_of_digits = 0
comparing_offset = 1
for i,x in enumerate(digit_sequence):
  if x == digit_sequence[(i + comparing_offset) % len(digit_sequence)]:
    sum_of_digits += int(x)
print(sum_of_digits)

