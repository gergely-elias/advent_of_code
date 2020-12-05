input_file = open("inputd17.txt", "r")
input_lines = input_file.readlines()

steps = int(input_lines[0].strip())
buffer_state = [0]
current_position = 0

for value_to_insert in range(1, 2018):
    current_position = (current_position + steps) % len(buffer_state) + 1
    buffer_state = (
        buffer_state[:current_position]
        + [value_to_insert]
        + buffer_state[current_position:]
    )
print(buffer_state[current_position + 1])
