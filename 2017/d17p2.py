input_file = open("inputd17.txt", "r")
input_lines = input_file.readlines()

steps = int(input_lines[0].strip())
buffer_length = 1
current_position = 0
value_after_zero = None

for value_to_insert in range(1, 50000001):
    current_position = (current_position + steps) % buffer_length + 1
    buffer_length += 1
    if current_position == 1:
        value_after_zero = value_to_insert
print(value_after_zero)
