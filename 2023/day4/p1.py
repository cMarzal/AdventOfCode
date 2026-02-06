import re
data = [[re.findall(r'\d+', line.split(":")[1].split("|")[0]), re.findall(r'\d+', line.split(":")[1].split("|")[1])] for line in open('inp').read().split('\n')]
tot = 0
for [t1, t2] in data:
    n = 0
    for x in t2:
        if x in t1:
            n = max(1, n*2)
    tot += n
print(tot)