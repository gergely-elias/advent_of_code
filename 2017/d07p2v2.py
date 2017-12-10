input_file = open('inputd07.txt','r')
input_lines = input_file.readlines()

import re

base_discs = set()
subtower_discs = set()
disc_properties = {}

for line in input_lines:
  discs = re.findall('\w+', line)
  base_discs.add(discs[0])
  subtower_discs.update(discs[2:])
  disc_properties[discs[0]] = {'self_weight': int(discs[1]), 'total_weight': 0, 'held_discs': discs[2:]}

bottom_disc = list(base_discs.difference(subtower_discs))[0]

def calculate_total_weight(disc):
  total_weight = disc_properties[disc]['self_weight']
  for held_disc in disc_properties[disc]['held_discs']:
    total_weight += calculate_total_weight(held_disc)
  disc_properties[disc]['total_weight'] = total_weight
  return total_weight

calculate_total_weight(bottom_disc)

unbalanced_disc = bottom_disc
misweighted_discs = True
while misweighted_discs:
  misweighted_discs = False
  held_discs = disc_properties[unbalanced_disc]['held_discs']
  held_disc_weights = [disc_properties[held_disc]['total_weight'] for held_disc in held_discs]
  held_disc_weights.sort()
  reference_weight = held_disc_weights[1]
  for held_disc in held_discs:
    if disc_properties[held_disc]['total_weight'] != reference_weight:
      weight_difference = disc_properties[held_disc]['total_weight'] - reference_weight
      unbalanced_disc = held_disc
      misweighted_discs = True
      break

print disc_properties[unbalanced_disc]['self_weight'] - weight_difference

