input_file = open('inputd14.txt','r')
input_lines = input_file.readlines()

word = input_lines[0].strip()

def knot_hash(key):
  n = 256
  current_position = 0
  number_list = range(n)
  lengths = [ord(x) for x in key]
  lengths += [17, 31, 73, 47, 23]
  skip_size = 0
  for round in range(64):
    for length in lengths:
      shifted_number_list = number_list[current_position:] + number_list[:current_position]
      part_to_reverse = shifted_number_list[:length]
      part_not_to_reverse = shifted_number_list[length:]
      part_to_reverse.reverse()
      shifted_number_list = part_to_reverse + part_not_to_reverse
      number_list = shifted_number_list[n - current_position:] + shifted_number_list[:n - current_position]

      current_position += length + skip_size
      current_position %= n
      skip_size += 1

  hash_digits = []
  for block_index in range(16):
    block = number_list[block_index * 16:(block_index + 1) * 16]
    xor_result = 0
    for number in block:
      xor_result ^= number
    hash_digits.append(('0' + hex(xor_result)[2:])[-2:])
  return ''.join(hash_digits)

size = 128
print sum([sum([int(digit) for digit in bin(int(knot_hash(word + '-' + str(row)),16))[2:].zfill(size)]) for row in range(size)])
