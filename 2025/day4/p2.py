data = [line for line in open('inp').read().split('\n')]
add_pos = (1,-1,1j,-1j,1+1j,1-1j,-1+1j,-1-1j)
tot_sum = 0
all_rolls = set([complex(x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "@"])
to_check = all_rolls.copy()
while to_check:
    roll = to_check.pop()
    this_set = set()
    for p in add_pos:
        if roll + p in all_rolls:
            this_set.add(roll + p)
    if len(this_set) < 4:
        tot_sum += 1
        all_rolls.remove(roll)
        to_check.update(this_set)

print(tot_sum)