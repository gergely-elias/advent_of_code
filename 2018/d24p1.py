input_file = open('inputd24.txt','r')
input_lines = input_file.readlines()

import re

def parse_attack_type_list(attack_types):
  return ''.join(attack_types).split(', ')

immune_system = []
infections = []
for line in input_lines:
  line = line.strip()
  if line == 'Immune System:':
    current_class = 0
    continue
  elif line == 'Infection:':
    current_class = 1
    continue
  elif line == '':
    continue
  number_of_units, hit_points, attack_damage, initiative = map(int, re.findall('\d+', line))
  immunity = parse_attack_type_list(re.findall('immune to ([\w\ ,]+)', line))
  weakness = parse_attack_type_list(re.findall('weak to ([\w\ ,]+)', line))
  attack_type = re.findall('(\w+) damage', line)[0]
  group = {'class': current_class,
           'units': number_of_units,
           'hp': hit_points,
           'damage': attack_damage,
           'attack_type': attack_type,
           'init': initiative,
           'weak': weakness,
           'immune': immunity,
           'power': number_of_units * attack_damage}
  if current_class == 0:
    immune_system.append(group)
  else:
    infections.append(group)

def calculate_damage_factor(defender_group, attack_type):
  if attack_type in defender_group['immune']:
    return 0
  elif attack_type in defender_group['weak']:
    return 2
  else:
    return 1

def find_group_with_initiative(groups, initiative):
  for index, group in enumerate(groups):
    if group['init'] == initiative:
      return index, group
  return -1

combat_over = False
while not combat_over:
  all_groups = immune_system + infections

  all_groups.sort(key = lambda group: (-group['power'], -group['init']))
  target = dict()
  for targetor_group in all_groups:
    attack_type = targetor_group['attack_type']
    attackable_opponents = [group for group in all_groups if group['class'] != targetor_group['class'] and not (group['init'] in target.values())]
    for defender_group in attackable_opponents:
      defender_group['damage_factor'] = calculate_damage_factor(defender_group, attack_type)
    attackable_opponents.sort(key = lambda opponent_lookup: (-opponent_lookup['damage_factor'], -opponent_lookup['power'], -opponent_lookup['init']))
    if len(attackable_opponents) > 0 and attackable_opponents[0]['damage_factor'] > 0:
      target[targetor_group['init']] = attackable_opponents[0]['init']

  all_groups.sort(key = lambda group: (-group['init']))
  for attacker_group in all_groups:
    if target.has_key(attacker_group['init']):
      opponent_lookup = find_group_with_initiative(all_groups, target[attacker_group['init']])
      if opponent_lookup[0] > -1:
        defender_group = opponent_lookup[1]
        attack_type = attacker_group['attack_type']
        defender_group['damage_factor'] = calculate_damage_factor(defender_group, attack_type)
        defender_group['units'] -= defender_group['damage_factor'] * attacker_group['power'] / defender_group['hp']
        defender_group['power'] = defender_group['units'] * defender_group['damage']
        if defender_group['units'] <= 0:
          opponents = [immune_system, infections][defender_group['class']]
          del opponents[find_group_with_initiative(opponents, defender_group['init'])[0]]
          target.pop(defender_group['init'])
          if len(opponents) == 0:
            combat_over = True

print sum([i['units'] for i in all_groups])
