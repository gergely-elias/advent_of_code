import fileinput

input_lines = list(fileinput.input())

line = input_lines[0].strip().split(",")
initial_order = [chr(i) for i in range(ord("a"), ord("p") + 1)]


def dance(order):
    order = order[:]
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
    return order


perms = [initial_order]
order = dance(initial_order)
while order != initial_order:
    perms.append(order)
    order = dance(order)
print("".join(perms[1000000000 % len(perms)]))
