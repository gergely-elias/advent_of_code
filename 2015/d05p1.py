input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

good_words = 0
for word in input_lines:
  if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word:
    #pass
    continue
  for i in range(len(word)-1):
    double_letter_found = False
    if word[i] == word[i+1]:
      double_letter_found = True
      break
  if not double_letter_found:
    continue
  num_of_vowels = 0
  for i in range(len(word)):
    if word[i] in 'aeiou':
      num_of_vowels += 1
  if num_of_vowels > 2:
    good_words += 1
print good_words

