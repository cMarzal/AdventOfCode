data = tuple(line for line in open('inp').read().split('\n'))
def find_group(let, pos, perimeter, this_seen):
    this_seen.add(pos)
    this_around = sum([1 if pos + p in this_seen else 0 for p in (1,-1,-1j,1j)])
    perimeter += 2 * (2-this_around)
    for s in (1,-1,-1j,1j):
        check_pos = pos + s
        try:
            if check_pos not in this_seen and check_pos.imag >= 0 and check_pos.real >= 0 and data[int(check_pos.imag)][int(check_pos.real)] == let:
                perimeter, this_seen = find_group(let, check_pos, perimeter, this_seen)
        except:
            pass
    return perimeter, this_seen
seen = set()
tot_sum = 0
for x, l in enumerate(data):
    for y, letter in enumerate(l):
        this_pos = complex(y, x)
        if this_pos not in seen:
            this_p, this_s = find_group(letter, this_pos, 0, set())
            seen.update(this_s)
            tot_sum += this_p * len(this_s)
print(tot_sum)
