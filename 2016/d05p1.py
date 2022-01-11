import fileinput
import hashlib

input_lines = list(fileinput.input())

door_id = input_lines[0].strip()
index = 0
password = ""
hashes_found = 0

while hashes_found < 8:
    checksum = hashlib.md5((door_id + str(index)).encode("utf-8")).hexdigest()
    if checksum[:5] == "00000":
        password += checksum[5]
        hashes_found += 1
    index += 1

print(password)
