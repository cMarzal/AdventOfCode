from heapq import heappop, heappush

data = {complex(y, x): int(value) for x, row in enumerate(open('inp').read().split('\n')) for y, value in enumerate(row)}

ind_value = 1
seen = set()
end_pos = [*data][-1]
our_heap = [(0,0,0,1),(0,1,0,1j)]
while our_heap:
    heat, _, pos, dir = heappop(our_heap)
    this_index = (pos,dir)
    if this_index in seen:
        continue
    elif pos == end_pos:
        print("final result: " + str(heat))
        break
    seen.add(this_index)
    this_dirs = (1*dir, -1*dir)
    for dirs in this_dirs:
        for l in range(4,11):
            new_pos = pos + (dirs*l)
            if new_pos in data:
                new_heat = heat + sum(data[pos + (dirs*p)] for p in range(1, l+1))
                ind_value += 1
                heappush(our_heap, (new_heat,ind_value,new_pos,dir*+1j))
            else:
                break
