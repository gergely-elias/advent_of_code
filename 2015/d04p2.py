import hashlib

secret_key = 'iwrupvqb'

i=0

while True:
  i += 1
  hashable = secret_key + str(i)
  hashresult = hashlib.md5(hashable).hexdigest()
  if hashresult[:6] == '000000':
    print hashable, hashresult
    break
