import fileinput

input_lines = list(fileinput.input())

report = [line.strip() for line in input_lines]
number_of_bits = len(report[0])


def filter_report_bit_by_bit(
    filtered_report, filter_bit_on_1_majority, filter_bit_on_0_majority
):
    bit_index = 0
    while len(filtered_report) > 1:
        bit_counter = 0
        for line in filtered_report:
            bit_counter += int(line[bit_index])
        if bit_counter >= len(filtered_report) / 2:
            filtered_report = [
                number
                for number in filtered_report
                if number[bit_index] == filter_bit_on_1_majority
            ]
        else:
            filtered_report = [
                number
                for number in filtered_report
                if number[bit_index] == filter_bit_on_0_majority
            ]
        bit_index += 1
    return filtered_report[0]


oxygen_generator_rating = filter_report_bit_by_bit(report, "1", "0")
co2_scrubber_rating = filter_report_bit_by_bit(report, "0", "1")

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))
