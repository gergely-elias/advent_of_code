import fileinput

input_lines = list(fileinput.input())

closing_opening_character_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
completion_character_score = {"(": 1, "[": 2, "{": 3, "<": 4}

completion_scores = []
for line in input_lines:
    line_is_corrupted = False
    stack_of_opening_characters = []
    for character in line.strip():
        if character in closing_opening_character_pairs.keys():
            last_opening_character = (
                ""
                if len(stack_of_opening_characters) == 0
                else stack_of_opening_characters.pop()
            )
            if last_opening_character != closing_opening_character_pairs[character]:
                line_is_corrupted = True
                break
        else:
            stack_of_opening_characters.append(character)
    if not line_is_corrupted:
        line_completion_score = 0
        for character in reversed(stack_of_opening_characters):
            line_completion_score = (
                line_completion_score * 5 + completion_character_score[character]
            )
        completion_scores.append(line_completion_score)

print(sorted(completion_scores)[len(completion_scores) // 2])
