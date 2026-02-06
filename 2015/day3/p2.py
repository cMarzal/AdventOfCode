dirs = open('inp').read()
dmap = {"<": -1, ">": 1, "^": -1j, "v": 1j}
pos1 = complex(0,0)
pos2 = complex(0,0)
houses = {pos1}
for a, b in zip(dirs[0::2], dirs[1::2]):
    pos1 += dmap[a]
    pos2 += dmap[b]
    houses.update({pos1,pos2})
print(len(houses))
