input_file = open('inputd04.txt','r')
input_lines = input_file.readlines()

my_range = list(map(int, input_lines[0].split('-')))

possible_passwords = 0
for password_candidate in range(my_range[0], my_range[1] + 1):
    digits = list(map(int, list(str(password_candidate))))
    sorted_digits = sorted(digits)
    digit_frequencies = [digits.count(x) for x in set(digits)]
    if digits == sorted_digits and max(digit_frequencies) >= 2:
      possible_passwords += 1
print(possible_passwords)
