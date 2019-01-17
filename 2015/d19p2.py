input_file = open('inputd19.txt','r')
input_lines = input_file.readlines()

import re
import collections

regex_start = None
regex_end = None
regex_separator = None

def classify(replacements):
  global regex_start, regex_end, regex_separator
  replacable_molecules = set([old for old, new in replacements])
  replacement_classes = collections.defaultdict(lambda: set())
  for old_submolecule, new_submolecule in replacements:
    if old_submolecule == 'e':
      replacement_classes[0].add(len(new_submolecule))
    else:
      if len(new_submolecule) > 2:
        if not (len(new_submolecule) % 2 != 0 or any([new_submolecule[i] in replacable_molecules for i in range(1, len(new_submolecule), 2)])) \
           and (regex_start == None or regex_start == new_submolecule[1]) \
           and (regex_end == None or regex_end == new_submolecule[-1]) \
           and (regex_separator == None or all([regex_separator == new_submolecule[i] for i in range(3, len(new_submolecule) - 3, 2)])):
          regex_start = new_submolecule[1]
          regex_end = new_submolecule[-1]
          regex_separator = new_submolecule[3] if len(new_submolecule) > 4 else regex_separator
          replacement_classes[1].add(len([atom in replacable_molecules for atom in new_submolecule]))
        else:
          exit()
      else:
        replacement_classes[1].add(len(new_submolecule))
  return replacement_classes

replacements = [(tuple(re.findall('\w+', line.strip()))) for line in input_lines[:-2]]
replacements = [(replacement[0], tuple(re.findall('[A-Z][a-z]*', replacement[1]))) for replacement in replacements]
molecule_length_changes = classify(replacements)
original_molecule = list(re.findall('[A-Z][a-z]*', input_lines[-1].strip()))
if(len(molecule_length_changes[0]) == 1 and min(molecule_length_changes[1]) == 2):
  print(len(original_molecule) - 2 * (original_molecule.count(regex_start) + original_molecule.count(regex_separator)) - (list(molecule_length_changes[0])[0] - 1))
