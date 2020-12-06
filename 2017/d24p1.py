import fileinput
import re

input_lines = list(fileinput.input())

edges = [list(map(int, re.findall("\d+", line.strip()))) for line in input_lines]


def trackback_edges(path, edges_left):
    vertices_left = set()
    for edge in edges_left:
        vertices_left.update(set(edge))
    if path[-1] not in vertices_left:
        yield path
    for edge in edges_left:
        if path[-1] in edge:
            edges_left_copy = edges_left[:]
            edges_left_copy.remove(edge)
            for longer_path in trackback_edges(
                path + [sum(edge) - path[-1]], edges_left_copy
            ):
                yield longer_path


print(max(2 * sum(bridge) - bridge[-1] for bridge in trackback_edges([0], edges)))
