from collections import defaultdict
from heapq import heappop, heappush

grid = {i+j*1j: c for i,r in enumerate(open('inp')) for j,c in enumerate(r) if c != '#'}

end_p, = (p for p in grid if grid[p] == 'E')
start, = (p for p in grid if grid[p] == 'S')
dist = defaultdict(lambda: 1e9)
todo = [(0, t:=0, end_p)]

while todo:
    val, _, pos = heappop(todo)
    if val > dist[pos]: continue
    else: dist[pos] = val
    for d in (1, -1, 1j, -1j):
        v, t, p = val+1, t+1, pos + d
        if p not in grid: continue
        heappush(todo, (v, t, p))

cheats = set()

for k, v in dist.items():
    for d in (1, -1, 1j, -1j):
        if k+d not in grid and k+2*d in dist and dist[k+2*d] < v - 100:
            cheats.add(k+d)
print(len(cheats))