import fileinput
import networkx
import re

input_lines = list(fileinput.input())

map_lines = [line.strip("\n") for line in input_lines[:-2]]
instructions = input_lines[-1].strip()

edge_length = 50

cubenet_graph = networkx.Graph()
for net_y, line in enumerate(map_lines[::edge_length]):
    for net_x, char in enumerate(line[::edge_length]):
        if char != " ":
            cubenet_graph.add_node((net_y, net_x))
            for possible_neighbour_on_net in [(net_y - 1, net_x), (net_y, net_x - 1)]:
                if possible_neighbour_on_net in cubenet_graph.nodes():
                    cubenet_graph.add_edge(possible_neighbour_on_net, (net_y, net_x))

cubenet_start_face = min(cubenet_graph.nodes())


class NeighbourAdjustment:
    def __init__(self, shift, flip, rotation):
        self.shift = shift
        self.flip = flip
        self.rotation = rotation


neighbour_adjustments = {
    (0, 1): NeighbourAdjustment(-1, False, -1),
    (1, 0): NeighbourAdjustment(1, True, 2),
    (0, -1): NeighbourAdjustment(-1, True, 2),
    (-1, 0): NeighbourAdjustment(1, False, 1),
}
directions_in_order = list(neighbour_adjustments.keys())


class FaceRepresentation:
    def __init__(self, face_vector, orientation, cubenet_coords):
        self.face_vector = face_vector
        self.orientation = orientation
        self.cubenet_coords = cubenet_coords


def tuple_sum(*args):
    return tuple(sum(coords) for coords in zip(*args))


def tuple_diff(tuple1, tuple2):
    return tuple(coord1 - coord2 for coord1, coord2 in zip(tuple1, tuple2))


def tuple_shift_left(mytuple, shift):
    return tuple(mytuple[shift % len(mytuple) :] + mytuple[: shift % len(mytuple)])


def tuple_flip(mytuple):
    return tuple(-coord for coord in mytuple)


def rotate_several_times(coords, times=1, clockwise=False):
    if clockwise:
        times = (-times) % len(directions_in_order)
    y, x = coords
    for _ in range(times):
        y, x = edge_length - 1 - x, y
    return y, x


face_representations_by_cubenet_coord = {
    cubenet_start_face: FaceRepresentation((0, 0, 1), 0, cubenet_start_face)
}
for (
    traversal_parent_cubenet_coord,
    traversal_children,
) in networkx.traversal.bfs_successors(cubenet_graph, cubenet_start_face):
    for traversal_child_cubenet_coord in traversal_children:
        child_from_parent_direction = tuple_diff(
            traversal_child_cubenet_coord, traversal_parent_cubenet_coord
        )
        if traversal_parent_cubenet_coord in face_representations_by_cubenet_coord:
            parent_orientation = face_representations_by_cubenet_coord[
                traversal_parent_cubenet_coord
            ].orientation
            child_from_reoriented_parent_direction = directions_in_order[
                (
                    directions_in_order.index(child_from_parent_direction)
                    - parent_orientation
                )
                % len(directions_in_order)
            ]
            neighbour_adjustment = neighbour_adjustments[
                child_from_reoriented_parent_direction
            ]
            parent_face_vector = face_representations_by_cubenet_coord[
                traversal_parent_cubenet_coord
            ].face_vector
            shifted_parent_face_vector = tuple_shift_left(
                parent_face_vector, sum(parent_face_vector) * neighbour_adjustment.shift
            )
            child_face_vector = (
                tuple_flip(shifted_parent_face_vector)
                if neighbour_adjustment.flip
                else shifted_parent_face_vector
            )
            child_orientation = (
                parent_orientation + neighbour_adjustment.rotation
            ) % len(directions_in_order)
            face_representations_by_cubenet_coord[
                traversal_child_cubenet_coord
            ] = FaceRepresentation(
                child_face_vector, child_orientation, traversal_child_cubenet_coord
            )

wall_coordinates = set()
for cube_net_y, cube_net_x in face_representations_by_cubenet_coord.keys():
    for y in range(edge_length * cube_net_y, edge_length * (cube_net_y + 1)):
        for x in range(edge_length * cube_net_x, edge_length * (cube_net_x + 1)):
            if map_lines[y][x] == "#":
                wall_coordinates.add(
                    (
                        face_representations_by_cubenet_coord[
                            cube_net_y, cube_net_x
                        ].face_vector,
                        *rotate_several_times(
                            (y % edge_length, x % edge_length),
                            times=face_representations_by_cubenet_coord[
                                cube_net_y, cube_net_x
                            ].orientation,
                            clockwise=False,
                        ),
                    )
                )


start_face_position = None
cube_net_y, cube_net_x = cubenet_start_face
for x in range(edge_length * cube_net_x, edge_length * (cube_net_x + 1)):
    if map_lines[0][x] == ".":
        start_face_position = rotate_several_times(
            (cube_net_y % edge_length, x % edge_length),
            times=face_representations_by_cubenet_coord[
                cube_net_y, cube_net_x
            ].orientation,
            clockwise=False,
        )
        break

assert instructions[0] not in "LR"
assert instructions[-1] not in "LR"
instructions += "N"
current_face_vector = (0, 0, 1)
position_on_cubeface = start_face_position
facing = 0
for path_fragment in re.findall(r"\d+[LNR]", instructions):
    amount = int(path_fragment[:-1])
    turn = path_fragment[-1]
    for _ in range(amount):
        next_face_vector = current_face_vector
        next_position_y, next_position_x = tuple_sum(
            directions_in_order[facing], position_on_cubeface
        )
        next_facing = facing
        if next_position_y == -1:
            next_face_vector = tuple_shift_left(
                current_face_vector, sum(current_face_vector)
            )
            next_position_y, next_position_x = (
                edge_length - 1 - next_position_x,
                edge_length - 1,
            )
            next_facing = 2
        elif next_position_x == -1:
            next_face_vector = tuple_flip(
                tuple_shift_left(current_face_vector, -sum(current_face_vector))
            )
            next_position_y, next_position_x = edge_length - 1 - next_position_y, 0
            next_facing = 0
        elif next_position_y == edge_length:
            next_face_vector = tuple_flip(
                tuple_shift_left(current_face_vector, sum(current_face_vector))
            )
            next_position_y, next_position_x = (
                edge_length - 1,
                edge_length - 1 - next_position_x,
            )
            next_facing = 3
        elif next_position_x == edge_length:
            next_face_vector = tuple_shift_left(
                current_face_vector, -sum(current_face_vector)
            )
            next_position_y, next_position_x = 0, edge_length - 1 - next_position_y
            next_facing = 1
        else:
            next_facing = facing

        if (next_face_vector, next_position_y, next_position_x) in wall_coordinates:
            break
        else:
            current_face_vector = next_face_vector
            position_on_cubeface = next_position_y, next_position_x
            facing = next_facing
    facing = (facing + "LNR".index(turn) - 1) % len(directions_in_order)

for face_representation in face_representations_by_cubenet_coord.values():
    if current_face_vector == face_representation.face_vector:
        cubenet_position = rotate_several_times(
            position_on_cubeface, times=face_representation.orientation, clockwise=True
        )
        final_row_index = (
            face_representation.cubenet_coords[0] * edge_length + cubenet_position[0]
        )
        final_column_index = (
            face_representation.cubenet_coords[1] * edge_length + cubenet_position[1]
        )
        final_facing = (facing + face_representation.orientation) % len(
            directions_in_order
        )
        print(
            1000 * (final_row_index + 1) + 4 * (final_column_index + 1) + final_facing
        )
        break
