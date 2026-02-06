data = tuple(line for line in open('inp').read().split('\n'))
def find_group(let, pos, perimeter, this_seen):
    this_seen.add(pos)
    this_around_pos = [p for p in (1,-1,-1j,1j) if pos + p in this_seen]
    this_around = len(this_around_pos)
    if this_around == 4:
        perimeter -= 4
    elif this_around == 3:
        for side in (1, -1, -1j, 1j):
            if side not in this_around_pos:
                this_diags = 1 if pos + side - (side * 1j) in this_seen else 0
                this_diags += 1 if pos + side + (side * 1j) in this_seen else 0
                perimeter -= 2 * (2 - this_diags)
                break
    elif this_around == 2:
        if this_around_pos[0] == -this_around_pos[1]:
            this_diags = len([p for p in (1+1j, -1+1j, 1-1j, -1-1j) if pos + p in this_seen])
            perimeter += 2*(this_diags-2)
        else:
            this_diags = 1 if pos + this_around_pos[0] - this_around_pos[1] in this_seen else 0
            this_diags += 1 if pos + this_around_pos[1] - this_around_pos[0] in this_seen else 0
            perimeter += 2 * (this_diags - 1)
    elif this_around == 1:
        for m in (1, -1, 1j, -1j):
            if pos + m in this_seen:
                tot_diag = sum([1 if pos + m + (m * cd) in this_seen else 0 for cd in (-1j, 1j)])
                perimeter += tot_diag * 2
                break
    else:
        perimeter += 4
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
