import fileinput

input_lines = list(fileinput.input())

closing_opening_character_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
illegal_character_score = {")": 3, "]": 57, "}": 1197, ">": 25137}

error_score = 0
for line in input_lines:
    stack_of_opening_characters = []
    for character in line.strip():
        if character in closing_opening_character_pairs.keys():
            last_opening_character = (
                ""
                if len(stack_of_opening_characters) == 0
                else stack_of_opening_characters.pop()
            )
            if last_opening_character != closing_opening_character_pairs[character]:
                error_score += illegal_character_score[character]
                break
        else:
            stack_of_opening_characters.append(character)

print(error_score)
