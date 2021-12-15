import fileinput
import networkx

input_lines = list(fileinput.input())
assert all([len(line) == len(input_lines[0]) for line in input_lines[1:]])
risk_levels = [list(map(int, line.strip())) for line in input_lines]

moves = networkx.DiGraph()
for row_index, row in enumerate(risk_levels):
    for column_index, risk_level in enumerate(row):
        if row_index > 0:
            moves.add_edge(
                (row_index - 1, column_index),
                (row_index, column_index),
                weight=risk_level,
            )
        if row_index < len(risk_levels):
            moves.add_edge(
                (row_index + 1, column_index),
                (row_index, column_index),
                weight=risk_level,
            )
        if column_index > 0:
            moves.add_edge(
                (row_index, column_index - 1),
                (row_index, column_index),
                weight=risk_level,
            )
        if column_index < len(risk_levels[row_index]):
            moves.add_edge(
                (row_index, column_index + 1),
                (row_index, column_index),
                weight=risk_level,
            )

print(
    networkx.shortest_path_length(
        moves, (0, 0), (len(risk_levels) - 1, len(risk_levels[-1]) - 1), weight="weight"
    )
)
