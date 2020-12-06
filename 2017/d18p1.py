import fileinput
import re
import collections

input_lines = list(fileinput.input())

instructions = [line.strip().split() for line in input_lines]
registers = collections.defaultdict(lambda: 0)
instruction_index = 0
last_sound_played = None


def substitute(value):
    if re.match("-?\d+", value):
        return int(value)
    return registers[value]


while instruction_index in range(0, len(instructions)):
    instruction = instructions[instruction_index]
    if instruction[0] == "set":
        registers[instruction[1]] = substitute(instruction[2])
    elif instruction[0] == "add":
        registers[instruction[1]] += substitute(instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] *= substitute(instruction[2])
    elif instruction[0] == "mod":
        registers[instruction[1]] %= substitute(instruction[2])
    elif instruction[0] == "jgz" and substitute(instruction[1]) > 0:
        instruction_index += substitute(instruction[2])
        continue
    elif instruction[0] == "rcv" and last_sound_played != 0:
        registers[instruction[1]] = last_sound_played
        break
    elif instruction[0] == "snd":
        last_sound_played = substitute(instruction[1])
    instruction_index += 1

print(last_sound_played)
