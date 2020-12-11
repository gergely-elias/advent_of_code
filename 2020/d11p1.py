import fileinput
import itertools

input_lines = list(fileinput.input())

seats = [list(line.strip()) for line in input_lines]
height = len(seats)
width = len(seats[0])
neighbour_directions = [
    (y, x) for y in range(-1, 2) for x in range(-1, 2) if y != 0 or x != 0
]

previous_seats = [["" for x in range(width)] for y in range(height)]
while previous_seats != seats:
    previous_seats = [[seats[y][x] for x in range(width)] for y in range(height)]
    occupied_seats = 0
    for seat_coords in itertools.product(range(height), range(width)):
        (y, x) = seat_coords
        if previous_seats[y][x] == ".":
            seats[y][x] = "."
        else:
            previous_occupied_neighbours = 0
            for neighbour_offset in neighbour_directions:
                neighbour_coord = (
                    seat_coords[0] + neighbour_offset[0],
                    seat_coords[1] + neighbour_offset[1],
                )
                (neighbour_y, neighbour_x) = neighbour_coord
                if (neighbour_y in range(height)) and (neighbour_x in range(width)):
                    previous_occupied_neighbours += (
                        1 if previous_seats[neighbour_y][neighbour_x] == "#" else 0
                    )
            if previous_seats[y][x] == "L" and previous_occupied_neighbours == 0:
                seats[y][x] = "#"
                occupied_seats += 1
            elif previous_seats[y][x] == "#" and previous_occupied_neighbours >= 4:
                seats[y][x] = "L"
            else:
                seats[y][x] = previous_seats[y][x]
                if previous_seats[y][x] == "#":
                    occupied_seats += 1
print(occupied_seats)
