data = [list(map(int, list(line))) for line in open('inp').read().split('\n')]
tot_sum = 0
for d in data:
    this_n = ""
    this_p = 0
    for n in range(12):
        end = n - 11 if n != 11 else None
        dn = max(d[this_p:end])
        this_p += d[this_p:end].index(dn) + 1
        this_n += str(dn)
    tot_sum += int(this_n)
print(tot_sum)
