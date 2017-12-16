input_file = open('inputd16.txt','r')
input_lines = input_file.readlines()

line = input_lines[0].strip().split(',')
order = [chr(i) for i in range(ord('a'), ord('p') + 1)]

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

print ''.join(order)
