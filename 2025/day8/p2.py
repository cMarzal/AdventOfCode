import math
from itertools import combinations

data = tuple(tuple(map(int, line.split(","))) for line in open('inp'))
closest = sorted(combinations(data, 2),key=lambda x: math.dist(*x))
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
    if len(connections) == 1 and len(connections[0]) == len(data):
        print(c1[0]*c2[0])
        break
    added_circ.update({c1,c2})
