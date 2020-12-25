import fileinput
import re

input_lines = list(fileinput.input())

replacements = [(tuple(re.findall(r"\w+", line.strip()))) for line in input_lines[:-2]]
original_molecule = input_lines[-1].strip()
new_molecules = set()
for old_submolecule, new_submolecule in replacements:
    matches = re.finditer(old_submolecule, original_molecule)
    for match in matches:
        replacement_result = (
            original_molecule[: match.span()[0]]
            + new_submolecule
            + original_molecule[match.span()[1] :]
        )
        new_molecules.add(replacement_result)
print(len(new_molecules))
