input_file = open("inputd03.txt", "r")
input_lines = input_file.readlines()

field_radius = 1000
field = (2 * field_radius + 1) * [0]
for i in range(2 * field_radius + 1):
    field[i] = (2 * field_radius + 1) * [0]
position = [field_radius + 1, field_radius + 1]
field[position[0]][position[1]] = 1

limit = int(input_lines[0].strip())
steps_in_one_direction = 0
coordinates_increasing = False
while True:
    steps_in_one_direction += 1
    coordinates_increasing = not coordinates_increasing
    for coordinate_axis in range(2):
        for step in range(steps_in_one_direction):
            position[coordinate_axis] = position[coordinate_axis] + (
                1 if coordinates_increasing else -1
            )
            current_field_value = (
                field[position[0] - 1][position[1] - 1]
                + field[position[0] - 1][position[1]]
                + field[position[0] - 1][position[1] + 1]
                + field[position[0]][position[1] - 1]
                + field[position[0]][position[1] + 1]
                + field[position[0] + 1][position[1] - 1]
                + field[position[0] + 1][position[1]]
                + field[position[0] + 1][position[1] + 1]
            )
            field[position[0]][position[1]] = current_field_value
            if current_field_value > limit:
                print(current_field_value)
                exit()
