import hashlib
inp = open('inp').read()
pas = ""
i= 0
for x in range(8):
    while not hashlib.md5(f'{inp}{str(i)}'.encode('latin-1')).hexdigest().startswith("00000"):
        i += 1
    pas += hashlib.md5(f'{inp}{str(i)}'.encode('latin-1')).hexdigest()[5]
    i+= 1
print(pas)

