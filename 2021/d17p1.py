import fileinput
import re
import itertools

input_lines = list(fileinput.input())
coord_ranges = {
    coord: (int(minval), int(maxval))
    for (coord, minval, maxval) in re.findall(
        r"(\w)=(-?\d+)\.\.(-?\d+)", input_lines[0]
    )
}

target_area_x = range(coord_ranges["x"][0], coord_ranges["x"][1] + 1)
target_area_y = range(coord_ranges["y"][0], coord_ranges["y"][1] + 1)
assert target_area_x[0] > 0
assert target_area_y[-1] < 0

initial_position = (0, 0)
highest_hitting_y_velocity = None
for initial_velocity in itertools.product(
    range(target_area_x[-1] + 1), range(target_area_y[0], -target_area_y[0] + 1)
):
    position_x, position_y = initial_position
    velocity_x, velocity_y = initial_velocity
    initial_velocity_y = velocity_y
    while (velocity_x > 0 and position_x < target_area_x[-1]) or (
        velocity_y > 0 or position_y > target_area_y[0]
    ):
        position_x += velocity_x
        position_y += velocity_y
        velocity_x = max(velocity_x - 1, 0)
        velocity_y -= 1
        if position_x in target_area_x and position_y in target_area_y:
            highest_hitting_y_velocity = (
                initial_velocity_y
                if highest_hitting_y_velocity is None
                or initial_velocity_y > highest_hitting_y_velocity
                else highest_hitting_y_velocity
            )
            break
print(highest_hitting_y_velocity * (highest_hitting_y_velocity + 1) // 2)
