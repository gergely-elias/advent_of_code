import fileinput
import itertools
import networkx
import re

input_lines = list(fileinput.input())
original_bricks = []
for line in input_lines:
    x1, y1, z1, x2, y2, z2 = map(int, re.findall(r"\d+", line))
    brick_coords = tuple(
        itertools.product(range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1))
    )
    original_bricks.append(brick_coords)
number_of_bricks = len(original_bricks)

is_below = networkx.DiGraph()
for brick_index in range(number_of_bricks):
    is_below.add_node(brick_index)
for (brick1_index, brick1), (brick2_index, brick2) in itertools.combinations(
    enumerate(original_bricks), 2
):
    for (x1, y1, z1), (x2, y2, z2) in itertools.product(brick1, brick2):
        if (x1, y1) == (x2, y2):
            if z1 < z2:
                is_below.add_edge(brick1_index, brick2_index)
            else:
                is_below.add_edge(brick2_index, brick1_index)
            break
assert networkx.is_directed_acyclic_graph(is_below)


def tuple_sum(*t):
    return tuple(sum(coords) for coords in zip(*t))


taken_coords = set()
final_positions = [None] * number_of_bricks
for brick_index in networkx.topological_sort(is_below):
    coords_before_fall = original_bricks[brick_index]
    coords_after_fall = tuple(
        tuple_sum(coords, (0, 0, -1)) for coords in coords_before_fall
    )
    while (
        len(set(coords_after_fall).intersection(taken_coords)) == 0
        and min(coords[2] for coords in coords_after_fall) >= 0
    ):
        coords_before_fall = coords_after_fall
        coords_after_fall = tuple(
            tuple_sum(coords, (0, 0, -1)) for coords in coords_before_fall
        )
    final_positions[brick_index] = coords_before_fall
    taken_coords.update(coords_before_fall)

direct_support = networkx.DiGraph()
for brick_index, brick in enumerate(final_positions):
    direct_support.add_node(brick_index)
    for upper_brick_index in is_below.successors(brick_index):
        for (x1, y1, z1), (x2, y2, z2) in itertools.product(
            brick, final_positions[upper_brick_index]
        ):
            if (x1, y1, z1) == (x2, y2, z2 - 1):
                direct_support.add_edge(brick_index, upper_brick_index)
                break

total_falling_count = 0
for brick_index in range(number_of_bricks):
    direct_support_copy = direct_support.copy()
    remove_queue = [brick_index]
    remove_count = 0
    while len(remove_queue):
        brick_to_remove = remove_queue.pop(0)
        remove_count += 1
        for holded in direct_support_copy.successors(brick_to_remove):
            if len(list(direct_support_copy.predecessors(holded))) == 1:
                remove_queue.append(holded)
        direct_support_copy.remove_node(brick_to_remove)
    total_falling_count += remove_count - 1
print(total_falling_count)
