import fileinput

input_lines = list(fileinput.input())

report = [line.strip() for line in input_lines]
report_length = len(report)
number_of_bits = len(report[0])

bit_counter = [0] * number_of_bits
for line in report:
    for bit_index in range(number_of_bits):
        bit_counter[bit_index] += int(line[bit_index])

gamma_rate = ""
epsilon_rate = ""
for bit_index in range(number_of_bits):
    if bit_counter[bit_index] > report_length / 2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
