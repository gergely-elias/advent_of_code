import fileinput
import hashlib

input_lines = list(fileinput.input())

secret_key = input_lines[0].strip()

i = 0
while True:
    i += 1
    hashable = secret_key + str(i)
    hashresult = hashlib.md5(hashable.encode("utf-8")).hexdigest()
    if hashresult[:6] == "000000":
        print(hashable[8:])
        break
