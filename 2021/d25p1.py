import fileinput

input_lines = list(fileinput.input())
seafloor = [list(line.strip()) for line in input_lines]

next_seafloor = []
step = 0
while next_seafloor != seafloor:
    step += 1
    next_seafloor = seafloor[:]
    for y in range(len(seafloor)):
        row = "".join(seafloor[y])
        row = row[-1] + row + row[0]
        row = row.replace(">.", ".>")
        row = row[1:-1]
        seafloor[y] = list(row)
    transposed_seafloor = list(zip(*seafloor))
    for x in range(len(transposed_seafloor)):
        column = "".join(transposed_seafloor[x])
        column = column[-1] + column + column[0]
        column = column.replace("v.", ".v")
        column = column[1:-1]
        transposed_seafloor[x] = column
    seafloor = list(zip(*transposed_seafloor))

print(step)
