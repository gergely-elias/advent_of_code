import fileinput
import networkx

input_lines = list(fileinput.input())
rules_lines, updates_lines = ("".join(input_lines)).strip().split("\n\n")

page_ordering = networkx.DiGraph()
for rule in rules_lines.split("\n"):
    page_ordering.add_edge(*map(int, rule.strip().split("|")))

total = 0
for update in updates_lines.split("\n"):
    updated_pages = list(map(int, update.strip().split(",")))
    if networkx.is_path(page_ordering, updated_pages):
        total += updated_pages[(len(updated_pages) - 1) // 2]
print(total)
