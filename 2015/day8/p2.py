data = tuple(line for line in open('inp').read().split('\n'))
tot_l = 0
tot_s = 0
for l in data:
    new_l = l.replace("\\", "\\\\").replace('"', '\\"')
    tot_l += len(l)
    tot_s += len(new_l) + 2
print(tot_l - tot_s)