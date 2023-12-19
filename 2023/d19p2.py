import collections
import copy
import fileinput
import math
import operator
import re

input_lines = list(fileinput.input())

workflows = ("".join(input_lines)).split("\n\n")[0]

starting_workflow = "in"
accepted_status = "A"
rejected_status = "R"
terminal_stati = {accepted_status, rejected_status}

operators = {"<": operator.lt, ">": operator.gt}
parsed_workflows = {}
for workflow in workflows.split("\n"):
    workflow_name, workflow_steps_joint = re.match(
        r"([A-Za-z]+)\{(.*)\}", workflow
    ).group(1, 2)
    workflow_steps = workflow_steps_joint.split(",")
    parsed_steps = []
    for step in workflow_steps[:-1]:
        parsed_step = re.match(r"([xmas])([<>])(\d+):([A-Za-z]+)", step).group(
            1, 2, 3, 4
        )
        parsed_steps.append(
            (
                parsed_step[0],
                operators[parsed_step[1]],
                int(parsed_step[2]),
                parsed_step[3],
            )
        )
    parsed_steps.append((None, None, None, workflow_steps[-1]))
    parsed_workflows[workflow_name] = parsed_steps

current_state = {starting_workflow: [{category: (1, 4000) for category in "xmas"}]}


def merge(*dictionaries):
    merged = collections.defaultdict(list)
    for d in dictionaries:
        for k in d.keys():
            merged[k] = merged[k] + d[k]
    return merged


def process(active_parts, active_rules):
    category, comparison, threshold, redirection = active_rules[0]
    if category is None:
        return {redirection: [active_parts]}
    else:
        interval_lower_bound, interval_upper_bound = active_parts[category]
        if comparison == operator.lt:
            if threshold > interval_upper_bound:
                return {redirection: [active_parts]}
            elif threshold <= interval_lower_bound:
                return process(active_parts, active_rules[1:])
            else:
                new_active_parts_in = copy.deepcopy(active_parts)
                new_active_parts_in[category] = (interval_lower_bound, threshold - 1)
                new_active_parts_out = copy.deepcopy(active_parts)
                new_active_parts_out[category] = (threshold, interval_upper_bound)
                return merge(
                    {redirection: [new_active_parts_in]},
                    process(new_active_parts_out, active_rules[1:]),
                )
        else:
            if threshold < interval_lower_bound:
                return {redirection: [active_parts]}
            elif threshold >= interval_upper_bound:
                return process(active_parts, active_rules[1:])
            else:
                new_active_parts_in = copy.deepcopy(active_parts)
                new_active_parts_in[category] = (threshold + 1, interval_upper_bound)
                new_active_parts_out = copy.deepcopy(active_parts)
                new_active_parts_out[category] = (interval_lower_bound, threshold)
                return merge(
                    {redirection: [new_active_parts_in]},
                    process(new_active_parts_out, active_rules[1:]),
                )


accepted_combinations_count = 0
while len(set(current_state).difference(terminal_stati)):
    next_state = collections.defaultdict(list)
    for active_workflow in current_state:
        active_rules = parsed_workflows[active_workflow]
        active_parts_list = current_state[active_workflow]
        for active_parts in active_parts_list:
            next_state = merge(next_state, process(active_parts, active_rules))
    for accepted_interval in next_state[accepted_status]:
        accepted_combinations_count += math.prod(
            high - low + 1 for low, high in accepted_interval.values()
        )
    current_state = {k: v for k, v in next_state.items() if k not in terminal_stati}
print(accepted_combinations_count)
