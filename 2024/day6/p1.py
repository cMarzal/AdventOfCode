data = [line for line in open('inp').read().split('\n')]
this_pos = 0
this_dir = 0
for y, l in enumerate(data):
    for x, c in enumerate(l):
        if c == "^":
            this_pos = complex(x,y)
            break
    if this_pos != 0:
        break
dirs = [-1j,1,1j,-1]
positions  = set()
positions.add(this_pos)
while True:
    positions.add(this_pos)
    new_pos = this_pos + dirs[this_dir % 4]
    try:
        if data[int(new_pos.imag)][int(new_pos.real)] == "#":
            this_dir += 1
        else:
            this_pos = new_pos
    except:
        break

print(len(positions))
