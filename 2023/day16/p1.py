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

ray_path(complex(0,-1),2)

this_checked = set([p[0] for p in pos_dirs])
print(len(this_checked)-1)
