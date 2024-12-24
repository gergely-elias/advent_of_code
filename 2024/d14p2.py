import fileinput
import re

input_lines = list(fileinput.input())
robots = [list(map(int, re.findall(r"-?\d+", line.strip()))) for line in input_lines]
width = 101
height = 103


def most_ordered_moment_by_axis(axis_index):
    axis_length = [width, height][axis_index]
    maximal_coord_count = 0
    for time in range(axis_length):
        current_coord_counts = [0 for _ in range(axis_length)]
        for start_coord, velocity_coord in [robot[axis_index::2] for robot in robots]:
            current_coord_counts[
                (start_coord + time * velocity_coord) % axis_length
            ] += 1
        if max(current_coord_counts) > maximal_coord_count:
            maximal_coord_count = max(current_coord_counts)
            most_ordered_moment = time
    return most_ordered_moment


print(
    (
        pow(height, width - 2, width) * width * most_ordered_moment_by_axis(1)
        + pow(width, height - 2, height) * height * most_ordered_moment_by_axis(0)
    )
    % (width * height)
)
