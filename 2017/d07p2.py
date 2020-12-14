import fileinput
import re
import copy

input_lines = list(fileinput.input())

disc_weights = {}
subtower_weights = {}
unknown_weight_subtowers = {}
known_weight_subtowers = {}

for line in input_lines:
    line = line.strip()
    line = re.findall("\w+", line)

    disc = line[0]
    weight = int(line[1])
    disc_weights[disc] = weight
    unknown_weight_subtowers[line[0]] = line[2:]
    known_weight_subtowers[line[0]] = []

original_subtowers = copy.deepcopy(unknown_weight_subtowers)

unbalanced_disc = None
reference_weight = 0

while True:
    for disc in unknown_weight_subtowers:
        if len(unknown_weight_subtowers[disc]) == 0:
            if len(known_weight_subtowers[disc]) > 0:
                weights_ordered = known_weight_subtowers[disc][:]
                weights_ordered.sort()
                if weights_ordered[0] == weights_ordered[-1]:
                    disc_to_remove = disc
                    weight_to_remove = (
                        disc_weights[disc]
                        + len(weights_ordered) * known_weight_subtowers[disc][0]
                    )
                    break
                else:
                    unbalanced_disc = disc
                    reference_weight = weights_ordered[1]
                    break
            elif len(known_weight_subtowers[disc]) == 0:
                disc_to_remove = disc
                weight_to_remove = disc_weights[disc]
                break

    if unbalanced_disc is None:
        unknown_weight_subtowers.pop(disc_to_remove)
        subtower_weights[disc_to_remove] = weight_to_remove
        for disc in unknown_weight_subtowers:
            if disc_to_remove in unknown_weight_subtowers[disc]:
                unknown_weight_subtowers[disc].remove(disc_to_remove)
                known_weight_subtowers[disc].append(weight_to_remove)
    else:
        for disc in original_subtowers[unbalanced_disc]:
            if subtower_weights[disc] != reference_weight:
                print(disc_weights[disc] + reference_weight - subtower_weights[disc])
        break
