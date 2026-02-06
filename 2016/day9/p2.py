data = open('inp').read().strip()
def ll(s):
    tot, c = 0, 0
    while True:
        if s[c] == "(":
            tr = s[c:].split("(")[1].split(")")[0].split("x")
            tot += int(tr[1])*ll(s[s.find(")",c)+1:s.find(")",c)+int(tr[0])+1])
            c = s.index(")", c)+int(tr[0])+1
        else:
            tot += 1
            c += 1
        if c >= len(s): return tot
print(ll(data))
