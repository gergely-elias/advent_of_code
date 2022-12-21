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
for monkey in yell_order:
    if monkey not in number_values:
        math_operator, prev_monkeys = math_operations[monkey]
        number_values[monkey] = math_operator(
            *[number_values[prev_monkey] for prev_monkey in prev_monkeys]
        )
root_value = number_values["root"]
assert root_value.denominator == 1
print(root_value)
