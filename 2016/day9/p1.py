data = open('inp').read().strip()
tot, c = 0, 0
while True:
    if data[c] == "(":
        tr = data[c:].split("(")[1].split(")")[0].split("x")
        tot += int(tr[0])*int(tr[1])
        c = data.index(")", c)+int(tr[0])+1
    else:
        tot += 1
        c += 1
    if c >= len(data): break
print(tot)
