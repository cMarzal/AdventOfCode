data = [mir for mir in open('inp').read().split('\n')]
mir_dict = {"|": (0,1,(0,1),(0,1)), "-": ((2,3), (2,3), 2, 3), "\\": (3, 2, 1, 0), "/": (2, 3, 0, 1)}
mir_pos = set([complex(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] != "."])
dirs = (-1,1,1j,-1j)
pos_dirs = set()
def ray_path(pos, di):
    while (pos, di) not in pos_dirs:
        pos_dirs.add((pos, di))
        pos = pos + dirs[di]
        if 0 <= pos.real < len(data) and 0 <= pos.imag < len(data[0]):
            if pos in mir_pos:
                di = mir_dict[data[int(pos.real)][int(pos.imag)]][di]
                if not isinstance(di, int):
                    for d in di:
                        ray_path(pos, d)
                    break
        else:
            break
max_seen = 0
for mm in range(len(data)):
    for xx in range(2):
        pos_dirs = set()
        if xx == 0:
            ray_path(complex(mm, -1), 2)
        else:
            ray_path(complex(mm, len(data[0])), 3)
        max_seen = max(len(set([p[0] for p in pos_dirs]))-1,max_seen)
for nn in range(len(data[0])):
    for yy in range(2):
        pos_dirs = set()
        if yy == 0:
            ray_path(complex(-1, nn), 1)
        else:
            ray_path(complex(len(data), nn), 0)
        max_seen = max(len(set([p[0] for p in pos_dirs]))-1,max_seen)

print(max_seen)
