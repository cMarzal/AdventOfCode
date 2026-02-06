data = tuple(line for line in open('inp').read().split('\n'))
tot_l = 0
tot_s = 0
for l in data:
    new_l = l[1:-1].encode("utf-8").decode("unicode_escape")
    tot_l += len(l)
    tot_s += len(new_l)
print(tot_l - tot_s)