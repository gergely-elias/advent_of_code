input_file = open('inputd01.txt','r')
input_lines = input_file.readlines()

word = input_lines[0].strip()
sum_of_digits = 0
comparing_offset = 1
for i in range(len(word)):
  if word[i] == word[(i + comparing_offset) % len(word)]:
    sum_of_digits += int(word[i])
print(sum_of_digits)

