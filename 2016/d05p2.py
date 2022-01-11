import fileinput
import hashlib

input_lines = list(fileinput.input())

door_id = input_lines[0].strip()
index = 0
password = list("________")
hashes_found = 0

while hashes_found < 8:
    checksum = hashlib.md5((door_id + str(index)).encode()).hexdigest()
    if checksum[:5] == "00000":
        password_index = int(checksum[5], 16)
        if password_index < 8 and password[password_index] == "_":
            password[password_index] = checksum[6]
            hashes_found += 1
    index += 1

print("".join(password))
