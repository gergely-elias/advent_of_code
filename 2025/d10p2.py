import fileinput
import re
import scipy.optimize

input_lines = list(fileinput.input())

total_button_presses = 0
for line in input_lines:
    match = re.search(r"\[(.*)\]\ (.*)\ \{(.*)\}", line.strip())
    buttons_raw, joltages_raw = match.group(2, 3)
    joltages = tuple(map(int, joltages_raw.split(",")))
    buttons = [
        tuple(map(int, button_raw[1:-1].split(",")))
        for button_raw in buttons_raw.split(" ")
    ]

    button_press_coefficients = [1 for _ in buttons]
    button_joltage_effect_matrix = [[0 for _ in buttons] for _ in joltages]
    for button_index, button in enumerate(buttons):
        for joltage_index in button:
            button_joltage_effect_matrix[joltage_index][button_index] = 1
    number_of_button_presses = int(
        sum(
            scipy.optimize.linprog(
                button_press_coefficients,
                A_eq=button_joltage_effect_matrix,
                b_eq=joltages,
                integrality=True,
            ).x
        )
    )

    total_button_presses += number_of_button_presses
print(total_button_presses)
