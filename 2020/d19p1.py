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
    if rule_index in literal:
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

print(sum([message in resolved_rules["0"] for message in message_lines]))
