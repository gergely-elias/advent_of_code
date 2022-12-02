import fileinput

input_lines = list(fileinput.input())

total_score = 0
for line in input_lines:
    their_play, outcome_code = line.strip().split()
    their_shape_index = ord(their_play) - ord("A")
    outcome_index = ord(outcome_code) - ord("X")
    my_shape_index = (their_shape_index + outcome_index - 1) % 3
    shape_score = my_shape_index + 1
    outcome_score = outcome_index * 3
    total_score += shape_score + outcome_score
print(total_score)
