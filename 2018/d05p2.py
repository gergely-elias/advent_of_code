import fileinput

input_lines = list(fileinput.input())

alphabet_length = ord("Z") - ord("A") + 1
uppercase_lowercase_code_offset = ord("a") - ord("A")
lengths = alphabet_length * [0]
polymer = list(input_lines[0].strip())


def react(chain):
    unit_index = 0
    while unit_index < len(chain) - 1:
        if (
            abs(ord(chain[unit_index]) - ord(chain[unit_index + 1]))
            == uppercase_lowercase_code_offset
        ):
            del chain[unit_index : unit_index + 2]
            unit_index = max(unit_index - 1, 0)
        else:
            unit_index += 1
    return chain


def remove(chain, letter_code):
    unit_index = 0
    while unit_index < len(chain):
        letter_offset = ord(chain[unit_index]) - letter_code
        if (letter_offset == 0) or (letter_offset == uppercase_lowercase_code_offset):
            del chain[unit_index]
        else:
            unit_index += 1
    return chain


reacted_polymer = react(polymer)[:]

for removed_letter_index in range(alphabet_length):
    polymer = reacted_polymer[:]
    removed_letter_code = ord("A") + removed_letter_index
    lengths[removed_letter_index] = len(react(remove(polymer, removed_letter_code)))

print(min(lengths))
