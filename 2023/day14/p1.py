data = [rocks for rocks in open('inp').read().split('\n')]
blocked = set()
rocks = []
for y in range(len(data)):
    for x in range(len(data[0])):
        char = data[y][x]
        if char == "#":
            blocked.add(complex(y, x))
        elif char == "O":
            rocks.append(complex(y, x))

to_check = [i for i in range(len(rocks))]
while to_check:
    r = to_check.pop(0)
    if (rocks[r]-1) not in blocked and (rocks[r]-1) not in rocks and rocks[r].real != 0:
        rocks[r] = rocks[r] - 1
        to_check.append(r)

print(int(sum([len(data) - rock.real for rock in rocks])))