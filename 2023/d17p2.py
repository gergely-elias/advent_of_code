import fileinput
import networkx

input_lines = list(fileinput.input())

city = [[int(char) for char in line.strip()] for line in input_lines]
height = len(city)
width = len(city[0])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
start_state = ((0, 0), (0, 0), 0)
finish_state = ((height - 1, width - 1), (0, 0), 0)
city_graph = networkx.DiGraph()


def tuple_sum(*t):
    return tuple(sum(coords) for coords in zip(*t))


straight_section_min_length = 4
straight_section_max_length = 10

for direction in directions:
    start_neighbour = tuple_sum(start_state[0], direction)
    city_graph.add_edge(
        start_state,
        (start_neighbour, direction, 1),
        weight=city[start_neighbour[0]][start_neighbour[1]],
    )

for y in range(height):
    for x in range(width):
        position = (y, x)
        for direction_index, direction in enumerate(directions):
            for straight in range(1, straight_section_max_length):
                if (
                    y == height - 1
                    and x == width - 1
                    and straight < straight_section_min_length
                ):
                    continue
                neighbour_y, neighbour_x = tuple_sum(direction, position)
                if neighbour_y in range(height) and neighbour_x in range(width):
                    city_graph.add_edge(
                        (position, direction, straight),
                        ((neighbour_y, neighbour_x), direction, straight + 1),
                        weight=city[neighbour_y][neighbour_x],
                    )
            for straight in range(
                straight_section_min_length, straight_section_max_length + 1
            ):
                if y == height - 1 and x == width - 1:
                    city_graph.add_edge(
                        (position, direction, straight), finish_state, weight=0
                    )
                    continue
                for neighbour_direction in [
                    directions[(direction_index + ndi) % len(directions)]
                    for ndi in [-1, 1]
                ]:
                    neighbour_y, neighbour_x = tuple_sum(neighbour_direction, position)
                    if neighbour_y in range(height) and neighbour_x in range(width):
                        city_graph.add_edge(
                            (position, direction, straight),
                            ((neighbour_y, neighbour_x), neighbour_direction, 1),
                            weight=city[neighbour_y][neighbour_x],
                        )

for direction in directions:
    for straight in range(straight_section_min_length, straight_section_max_length + 1):
        if (finish_state[0], direction, straight) in city_graph.nodes():
            city_graph.add_edge(
                (finish_state[0], direction, straight), finish_state, weight=0
            )

print(
    networkx.shortest_path_length(
        city_graph, start_state, finish_state, weight="weight"
    )
)
