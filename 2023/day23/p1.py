from collections import defaultdict
from heapq import heappop, heappush

data = tuple(group for group in open('inp').read().split('\n'))
route = {complex(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] != "#"}
slopes = {complex(i,j): data[i][j] for i in range(len(data)) for j in range(len(data[0])) if data[i][j] != "#" and data[i][j] != "."}
start = [complex(0,x) for x in range(len(data[0])) if data[0][x] == "."][0]
end = [complex(len(data)-1,x) for x in range(len(data[0])) if data[-1][x] == "."][0]
slope_dic = {">": 1j, "<": -1j, "v": 1, "^": -1}

dist = defaultdict(lambda: -1)
todo = [(0, t:=0, start, [])]

while todo:
    val, _, pos, path = heappop(todo)

    if val <= dist[pos]: continue
    dist[pos] = val
    path = path + [pos]

    for d in (1,-1,+1j,-1j):
        v, t, p = val+1, t+1, pos + d
        if p in route and p not in path:
            if p in slopes:
                path = path + [p]
                p = p + slope_dic[slopes[p]]
                v += 1
                if p == pos: continue
            heappush(todo, (v, t, p, path))

print(dist[end])