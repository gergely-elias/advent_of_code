input_file = open('inputd19.txt','r')
input_lines = input_file.readlines()

import re

replacements = [(tuple(re.findall('\w+', line.strip()))) for line in input_lines[:-2]]
original_molecule = input_lines[-1].strip()
new_molecules = set()
for old_submolecule, new_submolecule in replacements:
  matches = re.finditer(old_submolecule, original_molecule)
  for match in matches:
    replacement_result = original_molecule[:match.span()[0]] + new_submolecule + original_molecule[match.span()[1]:]
    new_molecules.add(replacement_result)
print(len(new_molecules))
