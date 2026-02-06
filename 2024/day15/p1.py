data = [block for block in open('inp').read().split('\n\n')]
map = data[0].split('\n')
dirs = data[1].replace("\n", "")
walls = set(complex(x,y) for y, line in enumerate(map) for x,l in enumerate(line) if l == "#")
boxes = set(complex(x,y) for y, line in enumerate(map) for x,l in enumerate(line) if l == "O")
pos = [complex(x,y) for y, line in enumerate(map) for x,l in enumerate(line) if l == "@"][0]
dmap = {"<": -1, ">": 1, "^": -1j, "v": 1j}
for d in dirs:
    this_d = dmap[d]
    new_pos = pos + this_d
    if new_pos not in walls:
        if new_pos not in boxes:
            pos = new_pos
        else:
            check_max = new_pos
            to_move = 1
            while True:
                check_max = check_max + this_d
                if check_max in walls:
                    break
                elif check_max not in boxes:
                    boxes.remove(new_pos)
                    boxes.add(check_max)
                    pos = new_pos
                    break
tot_sum = 0
for b in boxes:
    tot_sum += (100*b.imag) + b.real
print(tot_sum)