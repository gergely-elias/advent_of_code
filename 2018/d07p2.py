input_file = open('inputd07.txt','r')
input_lines = input_file.readlines()

import re

dependencies = []
tasks = set()
for line in input_lines:
  dependency = [task.strip() for task in re.findall('\ [A-Z]\ ', line.strip())]
  dependencies.append(dependency)
  tasks.update(dependency)

max_workers = 5
task_extra_time = 60

time = 0
tasks_in_progress = dict()
while True:
  just_finished_tasks = list(filter(lambda task: tasks_in_progress[task] == time, tasks_in_progress))
  tasks_in_progress = {k: v for k, v in tasks_in_progress.items() if v != time}

  just_finished_tasks.sort()
  tasks = tasks.difference(just_finished_tasks)
  dependencies = list(filter(lambda x: x[0] not in just_finished_tasks, dependencies))

  tasks_with_prerequirement = list(zip(*dependencies))[1] if len(dependencies) > 0 else []
  startable_tasks = sorted(list(tasks.difference(tasks_with_prerequirement).difference(set(tasks_in_progress))))
  free_workers = max_workers - len(tasks_in_progress)
  for task in startable_tasks[:free_workers]:
    tasks_in_progress[task] = time + task_extra_time + (ord(task) - ord('A') + 1)

  if len(tasks_in_progress) == 0:
    break
  time = min(tasks_in_progress.values())
print(time)
