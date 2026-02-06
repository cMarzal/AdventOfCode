data = [l for l in open('inp').read().split(", ")]
dirs = [1, 1j, -1, -1j]
this_dir, pos = 0, 0
for d in data:
    this_dir += 1 if d[0] == "R" else -1
    pos += dirs[this_dir%4]*int(d[1:])
print(int(abs(pos.imag)+abs(pos.real)))