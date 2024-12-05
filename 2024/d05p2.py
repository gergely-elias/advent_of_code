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
    if not networkx.is_path(page_ordering, updated_pages):
        page_subordering = page_ordering.subgraph(updated_pages)
        sorted_updates_pages = list(networkx.topological_sort(page_subordering))
        total += sorted_updates_pages[(len(sorted_updates_pages) - 1) // 2]
print(total)
