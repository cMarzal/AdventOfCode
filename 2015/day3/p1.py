dirs = open('inp').read()
dmap = {"<": -1, ">": 1, "^": -1j, "v": 1j}
this_pos = complex(0,0)
houses = {this_pos}
for d in dirs:
    this_pos += dmap[d]
    houses.add(this_pos)
print(len(houses))
