import fileinput
import re

input_lines = list(fileinput.input())

signal = list(map(int, list(re.findall("\d", input_lines[0]))))
signal *= 10000
offset = int("".join(map(str, signal[:7])))
assert offset >= len(signal) // 2
signal = signal[offset:]

n = len(signal)
for iteration in range(100):
    new_signal = [None] * n
    tail_sum = 0
    for signal_index in range(n):
        tail_sum += signal[n - 1 - signal_index]
        new_signal[n - 1 - signal_index] = abs(tail_sum) % 10
    signal = new_signal[:]

print("".join(map(str, signal[:8])))
