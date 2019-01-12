input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

good_words = 0
for word in input_lines:
  first_criterium_fulfilled = False
  for i in range(len(word)-2):
    if word[i] == word[i+2]:
      first_criterium_fulfilled = True
      break
  if not first_criterium_fulfilled:
    continue
  second_criterium_fulfilled = False
  for i in range(len(word)-3):
    for j in range(i+2,len(word)-1):
      if word[i:i+2] == word[j:j+2]:
        second_criterium_fulfilled = True
        break
    if second_criterium_fulfilled:
      break
  if second_criterium_fulfilled:
    good_words +=1
print(good_words)
