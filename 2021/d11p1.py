import fileinput

input_lines = list(fileinput.input())

number_of_rows = len(input_lines)
number_of_columns = len(input_lines[0].strip())

octopis_energies = {
    (y, x): int(input_lines[y][x])
    for y in range(number_of_rows)
    for x in range(number_of_columns)
}
neighbours_offsets = [
    (neighbour_y_offset, neighbour_x_offset)
    for neighbour_y_offset in range(-1, 1 + 1)
    for neighbour_x_offset in range(-1, 1 + 1)
    if any([coord != 0 for coord in (neighbour_y_offset, neighbour_x_offset)])
]
octopi_flashing = {coords: False for coords in octopis_energies.keys()}
total_steps = 100
max_non_flashing_energy = 9

number_of_flashes = 0
for step in range(total_steps):
    for coords in octopis_energies:
        octopis_energies[coords] += 1

    check_new_flash = True
    while check_new_flash:
        check_new_flash = False
        for coords in octopis_energies:
            if octopis_energies[coords] > max_non_flashing_energy:
                if not octopi_flashing[coords]:
                    for neighbour_coord in [
                        tuple(
                            sum(component_coord)
                            for component_coord in list(zip(coords, neighbour_offset))
                        )
                        for neighbour_offset in neighbours_offsets
                    ]:
                        if neighbour_coord in octopis_energies:
                            octopis_energies[neighbour_coord] += 1
                    octopi_flashing[coords] = True
                    check_new_flash = True

    for coords in octopis_energies:
        if octopi_flashing[coords]:
            number_of_flashes += 1
            octopi_flashing[coords] = False
            octopis_energies[coords] = 0

print(number_of_flashes)
