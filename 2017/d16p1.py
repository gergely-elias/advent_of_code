import fileinput

input_lines = list(fileinput.input())

line = input_lines[0].strip().split(",")
order = [chr(i) for i in range(ord("a"), ord("p") + 1)]

for move in line:
    if move[0] == "s":
        prg_idx = int(move[1:])
        order = order[-prg_idx:] + order[:-prg_idx]
    elif move[0] == "x":
        prg_idx_a, prg_idx_b = map(int, move[1:].split("/"))
        order[prg_idx_a], order[prg_idx_b] = order[prg_idx_b], order[prg_idx_a]
    elif move[0] == "p":
        prg_idx_a, prg_idx_b = map(order.index, move[1:].split("/"))
        order[prg_idx_a], order[prg_idx_b] = order[prg_idx_b], order[prg_idx_a]

print("".join(order))
