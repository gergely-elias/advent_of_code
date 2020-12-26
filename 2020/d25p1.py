import fileinput

input_lines = list(fileinput.input())

card_public_key = int(input_lines[0].strip())
door_public_key = int(input_lines[1].strip())

exponent = 0
power = 1
base = 7
modulus = 20201227
while True:
    exponent += 1
    power = (power * base) % modulus
    if power == card_public_key:
        print(pow(door_public_key, exponent, modulus))
        break
    elif power == door_public_key:
        print(pow(card_public_key, exponent, modulus))
        break
