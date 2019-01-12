input_file = open('inputd03.txt','r')
input_lines = input_file.readlines()

limit = int(input_lines[0].strip())
odd_squareroot = int((limit - 1) ** 0.5 + 1) // 2 * 2 - 1
corners_distance = odd_squareroot + 1
offset_from_corner = (limit - odd_squareroot ** 2) % (odd_squareroot + 1)
print(max(offset_from_corner, odd_squareroot + 1 - offset_from_corner))
