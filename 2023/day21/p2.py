from functools import cache

data = tuple(path for path in open('inp').read().split('\n'))
garden = {complex(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] != "#"}
start = [complex(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == "S"][0]

@cache
def get_next(pos):
    next_pos = set()
    for d in (1,-1,1j,-1j):
        if complex((d + pos).real%len(data),(d + pos).imag%len(data[0])) in garden:
            next_pos.add(d + pos)
    return next_pos

cur = {start}
times = 26501365
n_65 = 0
n_196 = 0
for x in range(327):
    if x == 196:
        n_196 = len(cur)
    if x == 65:
        n_65 = len(cur)
    new_cur = set()
    for c in cur:
        new_cur.update(get_next(c))
    cur = new_cur
diff_initial = n_196 - n_65
diff_cycle = (len(cur)-n_196) - (n_196 - n_65)
tot_sum = n_196
for i in range(int((times-196)/131)):
    tot_sum += diff_initial + ((i+1)*diff_cycle)
print(tot_sum)
