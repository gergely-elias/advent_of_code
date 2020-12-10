import fileinput

input_lines = list(fileinput.input())

adapters = [0] + [int(line.strip()) for line in input_lines]
adapters.sort()

maximal_difference = 3
number_of_arrangements = [1]
for adapter_index in range(1, len(adapters)):
    previous_adapters = adapters[:adapter_index][-maximal_difference:]
    number_of_arrangements_to_current_adapter = 0
    previous_adapters_compatible = [
        adapters[adapter_index] - previous_adapter <= maximal_difference
        for previous_adapter in previous_adapters
    ]
    previous_adapters_arrangements = number_of_arrangements[-maximal_difference:]
    number_of_arrangements.append(
        sum(
            [
                sub_arrangements if compatibility else 0
                for compatibility, sub_arrangements in zip(
                    previous_adapters_compatible, previous_adapters_arrangements
                )
            ]
        )
    )
print(number_of_arrangements[-1])
