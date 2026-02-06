data = [rocks for rocks in open('inp').read().split('\n')]
blocked = set()
rocks = []
for y in range(len(data)):
    blocked.add(complex(y, -1))
    blocked.add(complex(y, len(data[0])))
    for x in range(len(data[0])):
        blocked.add(complex(-1, x))
        blocked.add(complex(len(data), x))
        char = data[y][x]
        if char == "#":
            blocked.add(complex(y, x))
        elif char == "O":
            rocks.append(complex(y, x))
def to_rotate(dir_to, this_rocks):
    if dir_to == -1:
        this_rocks = sorted(this_rocks, key=lambda x: x.real)
    elif dir_to == -1j:
        this_rocks = sorted(this_rocks, key=lambda x: x.imag)
    elif dir_to == 1:
        this_rocks = sorted(this_rocks, key=lambda x: x.real, reverse=True)
    else:
        this_rocks = sorted(this_rocks, key=lambda x: x.imag, reverse=True)
    for r in range(len(this_rocks)):
        while True:
            if (this_rocks[r] + dir_to) not in blocked and (this_rocks[r] + dir_to) not in this_rocks:
                this_rocks[r] = this_rocks[r] + dir_to
            else:
                break
    return this_rocks

saved_pos = dict()
cicles = 1000000000
for x in range(1, cicles):
    for d in [-1,-1j,1,1j]:
        rocks = to_rotate(d, rocks)
    kk = tuple(rocks)
    if kk in saved_pos:
        prev_pos = saved_pos[kk]
        to_get_pos = (cicles-prev_pos)%(x-prev_pos) + prev_pos
        rocks = next(key for key, value in saved_pos.items() if value == to_get_pos)
        break
    else:
        saved_pos[kk] = x

print(int(sum([len(data) - rock.real for rock in rocks])))