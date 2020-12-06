import fileinput
import re

input_lines = list(fileinput.input())


def parse_line(line):
    fields = re.split("\W+", line)
    return {
        "min_count": int(fields[0]),
        "max_count": int(fields[1]),
        "letter": fields[2],
        "password": fields[3],
    }


passwords_with_policies = [parse_line(line) for line in input_lines]
print(
    sum(
        [
            entry["password"].count(entry["letter"])
            in range(entry["min_count"], entry["max_count"] + 1)
            for entry in passwords_with_policies
        ]
    )
)
