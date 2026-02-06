import re

data = [re.findall(r'\d+|blue|red|green', line) for line in open('inp').read().split('\n')]

tot_sum = 0

for d in data:
    this_d = dict()
    for x, s in enumerate(d):
        if not s.isnumeric():
            if s in this_d:
                this_d[s] = max(int(d[x -1]), this_d[s])
            else:
                this_d[s] = int(d[x -1])
    this_mp = 1
    for k in this_d.values():
        this_mp *= k
    tot_sum += this_mp

print(tot_sum)
