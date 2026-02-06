data = {line.split()[0]: (int(line.split()[3]), int(line.split()[6]), int(line.split()[13])+int(line.split()[6]))  for line in open('inp').read().split('\n')}

tot_sum = {x:[0, 0] for x in data.keys()}
for x in range(2503):
    for k, (v1,v2,v3) in data.items():
        if x%v3<v2:
            tot_sum[k][0] += v1
    this_max = max(v[0] for v in tot_sum.values())
    for k, v in tot_sum.items():
        if v[0] == this_max:
            tot_sum[k][1] += 1
print(max(v[1] for v in tot_sum.values()))