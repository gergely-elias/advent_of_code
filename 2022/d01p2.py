import fileinput

input_lines = list(fileinput.input())

elf_calories = [
    sum(map(int, elf_lines.split("\n")))
    for elf_lines in "".join(input_lines).strip().split("\n\n")
]

print(sum(sorted(elf_calories)[-3:]))
