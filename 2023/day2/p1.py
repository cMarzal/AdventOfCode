import re
aa = dict({"blue": 14, "green": 13, "red": 12})

data = [re.findall(r'\d+|blue|red|green', line) for line in open('inp').read().split('\n')]

tot_sum = 0

for d in data:
    add = 1
    for x, s in enumerate(d):
        if not s.isnumeric():
            if aa[s] < int(d[x -1]):
                add = 0
                break
    if add == 1:
       tot_sum += int(d[0])

print(tot_sum)
