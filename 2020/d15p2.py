import fileinput

input_lines = list(fileinput.input())

numbers = list(map(int, input_lines[0].strip().split(",")))
last_appearance = dict()
next_to_update = None
for turn, number in enumerate(numbers):
    next_to_update = turn - last_appearance[number] if number in last_appearance else 0
    last_appearance[number] = turn
for turn in range(len(numbers), 30000000 - 1):
    to_update = next_to_update
    next_to_update = (
        turn - last_appearance[to_update] if to_update in last_appearance else 0
    )
    last_appearance[to_update] = turn
print(next_to_update)
