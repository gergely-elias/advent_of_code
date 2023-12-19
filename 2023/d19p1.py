import fileinput
import operator
import re

input_lines = list(fileinput.input())

workflows, parts = ("".join(input_lines)).strip().split("\n\n")

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

rating_total = 0
for part in parts.split("\n")[:-1]:
    parsed_part = {}
    for part_fragment in part[1:-1].split(","):
        category, value = part_fragment[0], int(part_fragment[2:])
        parsed_part[category] = value
    part_rating = sum(parsed_part.values())
    active_workflow = starting_workflow
    while active_workflow not in terminal_stati:
        active_rules = parsed_workflows[active_workflow]
        for category, comparison, threshold, redirection in active_rules:
            if category is None:
                active_workflow = redirection
            else:
                if comparison(parsed_part[category], threshold):
                    active_workflow = redirection
                    break
    if active_workflow == accepted_status:
        rating_total += part_rating
print(rating_total)
