import fileinput
import re

input_lines = list(fileinput.input())

dependencies = []
tasks = set()
for line in input_lines:
    dependency = [task.strip() for task in re.findall(r"\ [A-Z]\ ", line.strip())]
    dependencies.append(dependency)
    tasks.update(dependency)

task_order = ""
while len(tasks) > 0:
    tasks_with_prerequirement = (
        list(zip(*dependencies))[1] if len(dependencies) > 0 else []
    )
    next_task = sorted(list(tasks.difference(tasks_with_prerequirement)))[0]
    task_order += "".join(next_task)
    tasks.discard(next_task)
    dependencies = list(filter(lambda x: x[0] != next_task, dependencies))
print(task_order)
