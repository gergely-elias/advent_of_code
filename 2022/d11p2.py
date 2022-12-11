import fileinput
import operator
import math

input_lines = list(fileinput.input())
lines_per_monkey = 6
monkeys = []
number_of_monkeys = (len(input_lines) + 1) // (lines_per_monkey + 1)
for monkey_index in range(number_of_monkeys):
    monkey_lines = [
        line.strip()
        for line in input_lines[
            monkey_index
            * (lines_per_monkey + 1) : (monkey_index + 1)
            * (lines_per_monkey + 1)
            - 1
        ]
    ]
    assert monkey_lines[0].startswith("Monkey ")
    assert int(monkey_lines[0][7:-1]) == monkey_index
    assert monkey_lines[1].startswith("Starting items:")
    monkey_items = list(map(int, monkey_lines[1].split(":")[1].split(",")))
    assert monkey_lines[2].startswith("Operation: new =")
    monkey_operation_rawtext = monkey_lines[2].split("=")[1].strip()
    assert monkey_operation_rawtext.startswith("old ")
    monkey_operation_args = monkey_operation_rawtext.split(" ")[1:]
    if monkey_operation_args[0] == "*":
        if monkey_operation_args[1] == "old":
            monkey_operation_operator = operator.pow
            monkey_operation_value = 2
        else:
            monkey_operation_operator = operator.mul
            monkey_operation_value = int(monkey_operation_args[1])
    elif monkey_operation_args[0] == "+":
        monkey_operation_operator = operator.add
        monkey_operation_value = int(monkey_operation_args[1])
    else:
        raise ValueError("operation cannot be parsed")
    assert monkey_lines[3].startswith("Test: divisible by ")
    monkey_test = int(monkey_lines[3].split(" ")[3])
    assert monkey_lines[4].startswith("If true: throw to monkey ")
    next_monkey_if_test_true = int(monkey_lines[4].split(" ")[5])
    assert monkey_lines[5].startswith("If false: throw to monkey ")
    next_monkey_if_test_false = int(monkey_lines[5].split(" ")[5])
    monkeys.append(
        (
            monkey_items,
            monkey_operation_operator,
            monkey_operation_value,
            monkey_test,
            next_monkey_if_test_true,
            next_monkey_if_test_false,
        )
    )

monkey_activities = [0 for _ in range(number_of_monkeys)]
number_of_rounds = 10000
worry_level_modulus = math.prod(monkey[3] for monkey in monkeys)

for round in range(number_of_rounds):
    for monkey_index in range(number_of_monkeys):
        (
            items,
            operation_operator,
            operation_value,
            test_modulus,
            next_monkey_if_test_true,
            next_monkey_if_test_false,
        ) = monkeys[monkey_index]
        while len(items) > 0:
            item_worry_level = items.pop(0)
            monkey_activities[monkey_index] += 1
            item_worry_level = operation_operator(item_worry_level, operation_value)
            item_worry_level %= worry_level_modulus
            next_monkey = (
                next_monkey_if_test_false
                if item_worry_level % test_modulus
                else next_monkey_if_test_true
            )
            monkeys[next_monkey][0].append(item_worry_level)
print(math.prod(sorted(monkey_activities)[-2:]))
