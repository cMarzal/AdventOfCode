data = {line for line in open('inp').read().split('\n')}
tot = 0
for d in data:
    c1, c2 = 0, 0
    for x in range(len(d)-2):
        if d[x:x+2] in d[x+2:]:
            c1 = 1
        if d[x] == d[x+2]:
            c2 = 1
        if c1 and c2:
            tot+=1
            break
print(tot)
