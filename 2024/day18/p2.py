from heapq import heappop, heappush

corr = [complex(int(line.split(",")[0]),int(line.split(",")[1])) for line in open('inp').read().split('\n')]
seen = 0
for bb in range(1024, len(corr)):
    if seen == 0 or corr[bb-1] in seen:
        print(bb)
        test = corr[bb]
        this_corr = corr[:bb]
        test2 = this_corr[-1]
        path = set(complex(i,j) for i in range(71) for j in range(71) if complex(i,j) not in this_corr)
        seen = set()
        todo = [(0, t:=0, 0)]
        done = 0

        while todo:
            _, _, pos = heappop(todo)
            if pos in seen: continue
            seen.add(pos)
            if pos == 70+70j:
                done = 1
                break
            for dir in (1, 1j, -1, -1j):
                l, t, p =  -pos.real -pos.imag, t+1, pos + dir
                if p in path and p not in seen:
                    heappush(todo, (l,t,p))
        if done == 0:
            print(this_corr[-1])
            break