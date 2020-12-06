import fileinput
import collections

input_lines = list(fileinput.input())

groups = " ".join([line.strip() for line in input_lines]).split("  ")
yes_questions = 0
for group in groups:
    counter = collections.Counter(group)
    counter.pop(" ", None)
    yes_questions += len(counter)
print(yes_questions)
