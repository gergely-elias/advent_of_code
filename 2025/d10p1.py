import fileinput
import itertools
import re

input_lines = list(fileinput.input())

total_button_presses = 0
for line in input_lines:
    match = re.search(r"\[(.*)\]\ (.*)\ \{(.*)\}", line.strip())
    indicators_raw, buttons_raw = match.group(1, 2)

    indicators = [indicator_char == "#" for indicator_char in indicators_raw]
    buttons = [
        tuple(map(int, button_raw[1:-1].split(",")))
        for button_raw in buttons_raw.split(" ")
    ]

    found = False
    for number_of_pressed_buttons in range(1, len(buttons) + 1):
        for pressed_buttons in itertools.combinations(
            buttons, number_of_pressed_buttons
        ):
            indicator_state = [False for _ in range(len(indicators_raw))]
            for pressed_button in pressed_buttons:
                for indicator_index in pressed_button:
                    indicator_state[indicator_index] = not indicator_state[
                        indicator_index
                    ]
            if indicator_state == indicators:
                found = True
                break
        if found:
            break
    total_button_presses += number_of_pressed_buttons
print(total_button_presses)
