import fileinput
import re

input_lines = list(fileinput.input())

sues = {}
for line in input_lines:
    current_sue = re.findall("\w+", line.strip())
    sue_properties = {}
    for i in range(2, len(current_sue), 2):
        sue_properties[current_sue[i]] = int(current_sue[i + 1])
    sues[int(current_sue[1])] = sue_properties

filters = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

sue_ids = set(sues.keys())
for sue_id in sues:
    skipsue = False
    for property_filter in filters:
        if property_filter in sues[sue_id]:
            if (
                (
                    (property_filter == "cats" or property_filter == "trees")
                    and sues[sue_id][property_filter] <= filters[property_filter]
                )
                or (
                    (property_filter == "pomeranians" or property_filter == "goldfish")
                    and sues[sue_id][property_filter] >= filters[property_filter]
                )
                or (
                    not (
                        property_filter == "cats"
                        or property_filter == "trees"
                        or property_filter == "pomeranians"
                        or property_filter == "goldfish"
                    )
                    and sues[sue_id][property_filter] != filters[property_filter]
                )
            ):
                sue_ids.remove(sue_id)
                skipsue = True
                break
    if skipsue:
        continue
print(list(sue_ids)[0])
