import itertools

data = {(line.split()[0],line.split()[-1][:-1],line.split()[2],line.split()[3]) for line in open('inp')}
info = {d[0]: {} for d in data}
for d1, d2, d3, d4 in data:
    info[d1][d2] = int(d4) if d3 == "gain" else -int(d4)
all_orders = set(itertools.permutations((x for x in info.keys())))

total_sum = 0
for it in all_orders:
    total_sum = max(total_sum, sum(info[it[x]][it[x-1]] + info[it[x]][it[(x+1)%len(it)]] for x in range(len(it))))
print(total_sum)

