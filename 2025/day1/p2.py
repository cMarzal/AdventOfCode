data_in = ((line[:1], int(line[1:])) for line in open('inp').read().split('\n'))
this_n = 50
tot_sum = 0
for l, n in data_in:
    prev = this_n
    this_n += n if l == "R" else -n
    if prev != 0:
        tot_sum += (-this_n/100)+1 if (this_n%100 == 0 and this_n <= 0) else int(abs((this_n - this_n%100) / 100))
    else:
        tot_sum += int(abs(n/100))
    this_n = this_n%100
print(tot_sum)
