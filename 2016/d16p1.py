import fileinput

input_lines = list(fileinput.input())

initial_state = input_lines[0].strip()
disk_length = 272

state = initial_state
while len(state) < disk_length:
    state = (
        state
        + "0"
        + "".join(reversed(list(state)))
        .replace("0", "x")
        .replace("1", "0")
        .replace("x", "1")
    )
checksum = state[:disk_length]
while len(checksum) % 2 == 0:
    checksum = "".join(
        [str(int(p1) ^ int(p2) ^ 1) for p1, p2 in zip(checksum[::2], checksum[1::2])]
    )
print(checksum)
