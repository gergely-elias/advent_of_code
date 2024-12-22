import enum
import fileinput
import networkx

input_lines = list(fileinput.input())
maze = [line.strip() for line in input_lines]
height = len(maze)
width = len(maze[0])

STEP_COST = 1
TURN_COST = 1000


class Directions(enum.Enum):
    NORTH = enum.auto()
    EAST = enum.auto()
    SOUTH = enum.auto()
    WEST = enum.auto()


DIRECTIONS_TO_COORDS = {
    Directions.NORTH: (-1, 0),
    Directions.EAST: (0, 1),
    Directions.SOUTH: (1, 0),
    Directions.WEST: (0, -1),
}

TURN_DIRECTIONS = {
    direction: [
        list(Directions)[
            (offset + list(Directions).index(direction)) % len(list(Directions))
        ]
        for offset in [1, -1]
    ]
    for direction in list(Directions)
}


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


maze_graph = networkx.DiGraph()
for y in range(height):
    for x in range(width):
        if maze[y][x] != "#":
            for direction in list(Directions):
                for turn_direction in TURN_DIRECTIONS[direction]:
                    maze_graph.add_edge(
                        (y, x, direction), (y, x, turn_direction), weight=TURN_COST
                    )
            for neighbour_direction in list(Directions):
                neighbour_y, neighbour_x = tuple_sum(
                    (y, x), DIRECTIONS_TO_COORDS[neighbour_direction]
                )
                if (
                    neighbour_y in range(height)
                    and neighbour_x in range(width)
                    and maze[neighbour_y][neighbour_x] != "#"
                ):
                    maze_graph.add_edge(
                        (y, x, neighbour_direction),
                        (neighbour_y, neighbour_x, neighbour_direction),
                        weight=STEP_COST,
                    )
        if maze[y][x] == "S":
            startpos = (y, x, Directions.EAST)
        if maze[y][x] == "E":
            endpos = (y, x)
            for direction in list(Directions):
                maze_graph.add_edge((y, x, direction), (y, x), weight=0)

tiles_on_paths = set().union(
    *networkx.all_shortest_paths(maze_graph, startpos, endpos, weight="weight")
)
print(len(set(tile[:2] for tile in tiles_on_paths)))
