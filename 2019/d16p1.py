input_file = open('inputd16.txt','r')
input_lines = input_file.readlines()

import re

base_pattern = [0, 1, 0, -1]
signal = list(map(int, list(re.findall('\d', input_lines[0]))))

n = len(signal)
for iteration in range(100):
  new_signal = [None] * n
  for signal_index in range(n):
    actual_pattern = [base_pattern[((pattern_index + 1) // (signal_index + 1)) % 4] for pattern_index in range(n)]
    new_signal[signal_index] = abs(sum([signal_digit * pattern_digit for (signal_digit, pattern_digit) in zip(signal, actual_pattern[:n])])) % 10
  signal = new_signal[:]

print(''.join(map(str, signal[:8])))
