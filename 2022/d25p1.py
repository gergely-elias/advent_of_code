import fileinput

snafu_digit_values = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
digit_snafu_representation = {v: k for k, v in snafu_digit_values.items()}
smallest_snafu_digit = min(digit_snafu_representation)
snafu_base = len(digit_snafu_representation)


def snafu_to_decimal(representation):
    return sum(
        [
            pow(snafu_base, index) * snafu_digit_values[snafu_digit]
            for index, snafu_digit in enumerate(reversed(representation))
        ]
    )


def decimal_to_snafu(value):
    snafu_representation = ""
    while value > 0:
        snafu_digit_value = (
            value - smallest_snafu_digit
        ) % snafu_base + smallest_snafu_digit
        value = (value - smallest_snafu_digit) // snafu_base
        snafu_representation = (
            digit_snafu_representation[snafu_digit_value] + snafu_representation
        )
    return snafu_representation


input_lines = list(fileinput.input())
total_fuel = sum([snafu_to_decimal(line.strip()) for line in input_lines])

print(decimal_to_snafu(total_fuel))
