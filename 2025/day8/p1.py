import math
from itertools import combinations

data = tuple(tuple(map(int, line.split(","))) for line in open('inp'))
pairs = sorted(combinations(data, 2),key=lambda x: math.dist(*x))
closest = tuple(pairs[:1000])
added_circ = set()
connections = []

for c1, c2 in closest:
    if c1 not in added_circ and c2 not in added_circ:
        connections.append({c1,c2})
    elif c1 in added_circ and c2 in added_circ:
        for con in connections:
            if c1 in con:
                if c2 not in con:
                    for con2 in connections:
                        if c2 in con2:
                            con.update(con2)
                            connections.remove(con2)
                            break
                break
    else:
        for con in connections:
            if c1 in con or c2 in con:
                con.update({c1,c2})
                break
    added_circ.update({c1,c2})

lengths = sorted(len(c) for c in connections)
print(math.prod(lengths[-3:]))
