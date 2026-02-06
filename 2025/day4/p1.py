data = [line for line in open('inp').read().split('\n')]
add_pos = (1,-1,1j,-1j,1+1j,1-1j,-1+1j,-1-1j)
tot_sum = 0
all_rolls = set([complex(x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "@"])
for roll in all_rolls:
    this_sur = sum([1 if roll+p in all_rolls else 0 for p in add_pos])
    if this_sur < 4: tot_sum += 1

print(tot_sum)