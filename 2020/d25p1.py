import fileinput

input_lines = list(fileinput.input())

card_public_key = int(input_lines[0].strip())
door_public_key = int(input_lines[1].strip())

exponent = 0
power = 1
base = 7
modulus = 20201227
card_private_key = None
door_private_key = None
while card_private_key is None or door_private_key is None:
    exponent += 1
    power = (power * base) % modulus
    if power == card_public_key:
        card_private_key = exponent
    elif power == door_public_key:
        door_private_key = exponent
print(pow(base, card_private_key * door_private_key, modulus))
