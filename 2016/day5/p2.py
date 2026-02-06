import hashlib
inp = open('inp').read()
pas = ["","","","","","","",""]
positions = {"1", "2", "3", "4", "5", "6", "7", "0"}
i = 0
while positions:
    while not hashlib.md5(f'{inp}{str(i)}'.encode('latin-1')).hexdigest().startswith("00000"):
        i += 1
    this_pos = hashlib.md5(f'{inp}{str(i)}'.encode('latin-1')).hexdigest()[5]
    if this_pos in positions:
        pas[int(this_pos)] = hashlib.md5(f'{inp}{str(i)}'.encode('latin-1')).hexdigest()[6]
        positions.remove(this_pos)
    i += 1
print("".join(pas))

