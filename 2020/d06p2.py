input_file = open("inputd06.txt", "r")
input_lines = input_file.readlines()

import collections

groups = " ".join([line.strip() for line in input_lines]).split("  ")
yes_questions = 0
for group in groups:
    counter = collections.Counter(group)
    number_of_people = counter.pop(" ", 0) + 1
    yes_questions += counter.values().count(number_of_people)
print(yes_questions)
