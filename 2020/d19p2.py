import fileinput
import networkx
import re
import itertools

input_lines = list(fileinput.input())

rule_block, message_block = "".join(input_lines).split("\n\n")
rule_lines = [line.strip() for line in rule_block.strip().split("\n")]
message_lines = [line.strip() for line in message_block.strip().split("\n")]

literal = dict()
rules = dict()
rule_dependencies = networkx.DiGraph()
for rule_line in rule_lines:
    rule_index, rule = list(map(lambda x: x.strip(), rule_line.split(":")))
    if rule.startswith('"'):
        literal[rule_index] = rule[1:-1]
    else:
        rules[rule_index] = rule
        referenced_rules = re.findall("\d+", rule)
        for referenced_rule in referenced_rules:
            rule_dependencies.add_edge(rule_index, referenced_rule)
order_of_rules = list(reversed(list(networkx.topological_sort(rule_dependencies))))

resolved_rules = dict()
for rule_index in order_of_rules:
    if rule_index in ["8", "11"]:
        assert networkx.ancestors(rule_dependencies, rule_index) == {"0"}
    elif rule_index == "0":
        assert rules[rule_index] == "8 11"
    elif rule_index in literal:
        resolved_rules[rule_index] = set([literal[rule_index]])
    else:
        accepted_strings = set()
        sub_rules = [sub_rule.strip() for sub_rule in rules[rule_index].split("|")]
        for sub_rule in sub_rules:
            accepted_strings = accepted_strings.union(
                [
                    "".join(accepted_substrings)
                    for accepted_substrings in list(
                        itertools.product(
                            *[
                                resolved_rules[referenced_rule]
                                for referenced_rule in sub_rule.split()
                            ]
                        )
                    )
                ]
            )
        resolved_rules[rule_index] = accepted_strings

possible_subrule_lengths = set(
    [len(x) for x in resolved_rules["42"]] + [len(x) for x in resolved_rules["31"]]
)
assert len(possible_subrule_lengths) == 1

unit_length = possible_subrule_lengths.pop()

number_of_matching_messages = 0
for message in message_lines:
    sliced_message = [
        message[unit_start : unit_start + unit_length]
        for unit_start in range(0, len(message), unit_length)
    ]
    number_of_slices = len(sliced_message)
    if any(
        [
            all(
                [
                    substring in resolved_rules[x]
                    for substring, x in zip(
                        sliced_message, ["42"] * k + ["31"] * (number_of_slices - k)
                    )
                ]
            )
            for k in range(number_of_slices // 2 + 1, number_of_slices)
        ]
    ):
        number_of_matching_messages += 1
print(number_of_matching_messages)
