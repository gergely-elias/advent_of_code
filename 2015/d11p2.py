input_file = open('inputd11.txt','r')
input_lines = input_file.readlines()

import string
import itertools

alphabet = string.ascii_lowercase
forbidden_characters = ['i', 'o', 'l']
forbidden_charcodes = [alphabet.index(char) for char in forbidden_characters]
smallest_valid_charcode = min(set(range(len(alphabet))).difference(forbidden_charcodes))

def step(converted_password, index):
  converted_password[index] += 1
  if converted_password[index] in forbidden_charcodes:
    converted_password[index] += 1
  if converted_password[index] == len(alphabet):
    converted_password[index] = smallest_valid_charcode
    converted_password = step(converted_password, index - 1)
  return converted_password

def jump_to_valid_word(converted_password):
  for index,charcode in enumerate(converted_password):
    if charcode in forbidden_charcodes:
      return step(converted_password, index)[:index + 1] + [smallest_valid_charcode] * (len(converted_password) - index - 1)
  return step(converted_password, -1)

def is_valid_word(converted_password):
  charcode_diffs = [j - i for i,j in zip(converted_password[:-1], converted_password[1:])]
  pair_positions = [i for i,x in enumerate(charcode_diffs) if x == 0]
  if len(pair_positions) > 2 or (len(pair_positions) == 2 and pair_positions[1] - pair_positions[0] != 1):
    straight_positions = [i for i,x in enumerate(charcode_diffs) if x == 1]
    straight_position_diffs = [l - k for k,l in zip(straight_positions[:-1], straight_positions[1:])]
    return 1 in straight_position_diffs
  return False

password = input_lines[0].strip()
converted_password = [alphabet.index(letter) for letter in password]
converted_password = jump_to_valid_word(converted_password)

skip_counter = 1
while not is_valid_word(converted_password) or skip_counter > 0:
  if is_valid_word(converted_password):
    skip_counter -= 1
  step(converted_password, -1)
print(''.join([alphabet[char_code] for char_code in converted_password]))
