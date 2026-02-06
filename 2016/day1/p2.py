data = [l for l in open('inp').read().split(", ")]
dirs = [1, 1j, -1, -1j]
this_dir, pos = 0, 0
seen_pos = set()
for d in data:
    this_dir = this_dir+1 if d[0] == "R" else this_dir-1
    for _ in range(int(d[1:])):
        pos += dirs[this_dir%4]
        if pos in seen_pos:
            print(int(abs(pos.imag)+abs(pos.real)))
            exit()
        seen_pos.add(pos)
