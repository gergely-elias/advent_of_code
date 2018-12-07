input_file = open('inputd04.txt','r')
input_lines = input_file.readlines()

import collections
import re

minutes_asleep = collections.defaultdict(lambda: 0)
guards_cumulated = collections.defaultdict(lambda: 0)

sorted_input = sorted(input_lines)
for line in sorted_input:
  line = line.strip()
  timestamp = map(int, re.findall('\d+', line[:19]))
  action = line[19:]
  if action[:5] == 'Guard':
    guard_id = int(re.findall('\d+', action)[0])
  elif action[:5] == 'falls':
    sleep_start = timestamp[4]
  else:
    sleep_end = timestamp[4]
    for minute in range(sleep_start, sleep_end):
      minutes_asleep[(guard_id, minute)] += 1
    guards_cumulated[guard_id] += sleep_end - sleep_start - 1

sleepy_guard = max(guards_cumulated, key = lambda guard: guards_cumulated[guard])
his_minutes = {minute: minutes_asleep[(guard, minute)] for (guard, minute) in minutes_asleep if guard == sleepy_guard}
sleepy_minute = max(his_minutes, key = lambda minute: his_minutes[minute])
print sleepy_guard * sleepy_minute 