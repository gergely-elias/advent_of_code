input_file = open('inputd05.txt','r')
input_lines = input_file.readlines()

alphabet_length = ord('Z') - ord('A') + 1
uppercase_lowercase_code_offset = ord('a') - ord('A')
lengths = alphabet_length * [0]
polymer = list(input_lines[0].strip())

def react(chain):
  i = 0
  while i < len(chain) - 1:
    if abs(ord(chain[i]) - ord(chain[i + 1])) == uppercase_lowercase_code_offset:
      del chain[i:i + 2]
      i = max(i - 1, 0)
    else:
      i += 1
  return chain

def remove(chain, letter_code):
  i = 0
  while i < len(chain):
    letter_offset = ord(chain[i]) - letter_code
    if (letter_offset == 0) or (letter_offset == uppercase_lowercase_code_offset):
      del chain[i]
    else:
      i += 1
  return chain

reacted_polymer = react(polymer)[:]

for removed_letter_index in range(alphabet_length):
  polymer = reacted_polymer[:]
  removed_letter_code = ord('A') + removed_letter_index
  lengths[removed_letter_index] = len(react(remove(polymer, removed_letter_code)))

print min(lengths)
