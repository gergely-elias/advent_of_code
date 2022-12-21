import fileinput
import networkx
import re
import operator
import fractions

input_lines = list(fileinput.input())
monkey_dependencies = networkx.DiGraph()
number_values = dict()
math_operations = dict()

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

for line in input_lines:
    line = line.strip().split(":")
    if re.match(r"^\ \d+$", line[1]):
        number_values[line[0]] = fractions.Fraction(line[1])
    else:
        math_operation_raw = line[1][1:].split()
        monkey_dependencies.add_edge(line[0], math_operation_raw[0])
        monkey_dependencies.add_edge(line[0], math_operation_raw[2])
        math_operations[line[0]] = (
            operators[math_operation_raw[1]],
            (math_operation_raw[0], math_operation_raw[2]),
        )

yell_order = list(reversed(list(networkx.topological_sort(monkey_dependencies))))
linear_coeff = fractions.Fraction(1, 1)
constant_coeff = fractions.Fraction(0, 1)

depending_on_human = {"humn"}
for monkey in yell_order:
    if monkey not in number_values:
        math_operator, prev_monkeys = math_operations[monkey]
        prev_monkeys_depending_on_human = depending_on_human.intersection(prev_monkeys)
        if len(prev_monkeys_depending_on_human) > 0:
            assert len(prev_monkeys_depending_on_human) == 1
            human_depending_monkey = prev_monkeys_depending_on_human.pop()
            human_depending_monkey_index = prev_monkeys.index(human_depending_monkey)
            non_human_depending_monkey_index = 1 - human_depending_monkey_index
            non_human_depending_monkey_number_value = number_values[
                prev_monkeys[non_human_depending_monkey_index]
            ]
            if monkey == "root":
                human_value = (
                    non_human_depending_monkey_number_value - constant_coeff
                ) / linear_coeff
                assert human_value.denominator == 1
                print(human_value)
                break
            if math_operator == operator.add:
                constant_coeff += non_human_depending_monkey_number_value
            elif math_operator == operator.mul:
                linear_coeff *= non_human_depending_monkey_number_value
                constant_coeff *= non_human_depending_monkey_number_value
            elif math_operator == operator.sub:
                constant_coeff -= non_human_depending_monkey_number_value
                if human_depending_monkey_index == 1:
                    constant_coeff *= -1
                    linear_coeff *= -1
            else:
                assert math_operator == operator.truediv
                assert human_depending_monkey_index == 0
                linear_coeff /= non_human_depending_monkey_number_value
                constant_coeff /= non_human_depending_monkey_number_value
            depending_on_human.add(monkey)
        else:
            number_values[monkey] = math_operator(
                *[number_values[prev_monkey] for prev_monkey in prev_monkeys]
            )
