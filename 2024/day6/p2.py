data = [line for line in open('inp').read().split('\n')]
start_pos = 0
this_dir = 0
for y, l in enumerate(data):
    for x, c in enumerate(l):
        if c == "^":
            start_pos = complex(x,y)
            break
    if start_pos != 0:
        break
dirs = [-1j,1,1j,-1]
tot_sum = 0
positions  = set()
this_pos = start_pos

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
for pos in positions:
    if pos != start_pos:
        this_pos = start_pos
        this_dir = 0
        new_data = data.copy()
        new_data[int(pos.imag)] = data[int(pos.imag)][:int(pos.real)] + "#" + data[int(pos.imag)][int(pos.real) + 1:]
        all_checked = set()
        while True:
            this_key = str(this_pos) + str(this_dir)
            if this_key in all_checked:
                tot_sum += 1
                break
            all_checked.add(this_key)
            new_pos = this_pos + dirs[this_dir]
            try:
                if new_data[int(new_pos.imag)][int(new_pos.real)] == "#":
                    this_dir = (this_dir + 1) % 4
                else:
                    this_pos = new_pos
            except:
                break
print(tot_sum)