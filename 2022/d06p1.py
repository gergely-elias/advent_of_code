import fileinput

input_lines = list(fileinput.input())

buffer = input_lines[0].strip()
message_length = 4
for start_position in range(len(buffer) - message_length + 1):
    if (
        len(set(buffer[start_position : start_position + message_length]))
        == message_length
    ):
        print(start_position + message_length)
        break
