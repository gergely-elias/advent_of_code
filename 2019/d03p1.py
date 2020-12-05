input_file = open("inputd03.txt", "r")
input_lines = input_file.readlines()

import re
import copy

wires = []
for line_index in range(len(input_lines)):
    wire = input_lines[line_index].strip().split(",")
    pos_list = [{"x": 0, "y": 0, "d": 0}]
    for instruction in wire:
        direction = ["U", "R", "D", "L"].index(instruction[0])
        distance = int(instruction[1:])
        last_pos = pos_list[-1]
        next_pos = last_pos.copy()
        next_pos[["y", "x"][direction % 2]] = last_pos[
            ["y", "x"][direction % 2]
        ] + distance * (1 - (direction // 2) * 2)
        next_pos["d"] = last_pos["d"] + distance
        pos_list.append(next_pos)
    wires.append(pos_list)


def intersection(part0, part1, axis):
    part0_sorted = sorted([part0[0][axis], part0[1][axis]])
    part1_sorted = sorted([part1[0][axis], part1[1][axis]])
    if (part0_sorted[0] - part1_sorted[1]) * (part1_sorted[0] - part0_sorted[1]) <= 0:
        return None
    return part0_sorted[0] if part0_sorted[0] == part0_sorted[1] else part1_sorted[0]


minimal_distance = float("inf")
for wire0_part_index in range(len(wires[0]) - 1):
    wire0_part = [wires[0][wire0_part_index], wires[0][wire0_part_index + 1]]
    for wire1_part_index in range(len(wires[1]) - 1):
        wire1_part = [wires[1][wire1_part_index], wires[1][wire1_part_index + 1]]
        intersection_x = intersection(wire0_part, wire1_part, "x")
        intersection_y = intersection(wire0_part, wire1_part, "y")
        if intersection_x is not None and intersection_y is not None:
            current_distance = abs(intersection_x) + abs(intersection_y)
            if current_distance < minimal_distance:
                minimal_distance = current_distance
print(minimal_distance)
