from itertools import combinations
import math

data = {int(line) for line in open('inp')}

tot = sum(data)
tot_size = tot//4
combos = []

for r in range(1, len(data)//4):
    for combo in combinations(data, r):
        if sum(combo) == tot_size:
            combos.append(combo)
    if combos: break

new_data = list(data)
min_prod = 99999999999
for c in combos:
    new_data = data.copy()
    for cx in c:
        new_data.remove(cx)
    for r in range(1, len(new_data)-3):
        stop = 0
        for combo in combinations(new_data, r):
            if sum(combo) == tot_size:
                min_prod = min(min_prod, math.prod(c))
                stop = 1
                break
        if stop: break

print(min_prod)

