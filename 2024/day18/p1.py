from collections import defaultdict
from heapq import heappop, heappush

corr = [complex(int(line.split(",")[0]),int(line.split(",")[1])) for line in open('inp').read().split('\n')]
this_corr = corr[:1024]
path = set(complex(i,j) for i in range(71) for j in range(71) if complex(i,j) not in this_corr)
best = 1e9
dist = defaultdict(lambda: 1e9)
todo = [(0, t:=0, 0)]

while todo:
    val, _, pos = heappop(todo)
    if val >= dist[pos]: continue
    else: dist[pos] = val
    if pos == 70+70j:
        best = val
    for dir in (1, -1, 1j, -1j):
        t, p = t+1, pos + dir
        if p in path:
            heappush(todo, (val+1, t, p))

print(best)