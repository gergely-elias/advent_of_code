input_file = open('inputd16.txt','r')
input_lines = input_file.readlines()

line = input_lines[0].strip().split(',')
initial_order = [chr(i) for i in range(ord('a'), ord('p') + 1)]

def dance(order):
  order = order[:]
  for move in line:
    if move[0] == 's':
      k = int(move[1:])
      order = order[-k:] + order[:-k]
    elif move[0] == 'x':
      k,l = map(int, move[1:].split('/'))
      order[k], order[l] = order[l], order[k]
    elif move[0] == 'p':
      k,l = map(order.index, move[1:].split('/'))
      order[k], order[l] = order[l], order[k]
  return order

perms = [initial_order]
order = dance(initial_order)
while order != initial_order:
  perms.append(order)
  order = dance(order)
print(''.join(perms[1000000000 % len(perms)]))
