data = [list(map(int, line)) for line in open('inp').read().split('\n')]
start_pos = list()
checks = [1,-1,-1j,1j]
for x, l in enumerate(data):
    for y, n in enumerate(l):
        if n == 0:
            start_pos.append(complex(y, x))
def keep_check(pos, num):
    this_sum = 0
    for c in checks:
        new_pos = pos + c
        try:
            if new_pos.imag >= 0 and new_pos.real >= 0 and data[int(new_pos.imag)][int(new_pos.real)] == num + 1:
                if num == 8:
                    this_sum += 1
                else:
                    this_sum += keep_check(new_pos, num+1)
        except:
            pass
    return this_sum
tot_sum = 0
for p in start_pos:
    this_seen = keep_check(p, 0)
    tot_sum += this_seen
print(tot_sum)