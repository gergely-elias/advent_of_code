import collections
import fileinput

input_lines = list(fileinput.input())
steps = input_lines[0].strip().split(",")


def hash_string(s):
    hash_value = 0
    for c in s:
        hash_value += ord(c)
        hash_value *= 17
        hash_value %= 256
    return hash_value


lenses_in_boxes = collections.defaultdict(dict)
for step in steps:
    if step.endswith("-"):
        label = step[:-1]
        box = hash_string(label)
        if label in lenses_in_boxes[box]:
            del lenses_in_boxes[box][label]
    else:
        operator_index = step.index("=")
        label = step[:operator_index]
        focal_length = int(step[operator_index + 1 :])
        box = hash_string(label)
        lenses_in_boxes[box][label] = focal_length

print(
    sum(
        (box + 1)
        * sum(
            (lens_index + 1) * lenses[label] for lens_index, label in enumerate(lenses)
        )
        for box, lenses in lenses_in_boxes.items()
    )
)
