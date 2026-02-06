import hashlib
inp = open('inp').read()
i = 0
while not hashlib.md5(f'{inp}{str(i)}'.encode('latin-1')).hexdigest().startswith("000000"):
    i += 1
print(i)