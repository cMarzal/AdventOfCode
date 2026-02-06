data_in = ((line[:1], int(line[1:])) for line in open('inp').read().split('\n'))
this_n = 50
tot_sum = 0
for l, n in data_in:
    this_n = (this_n + n) % 100 if l == "R" else (this_n - n) % 100
    if this_n == 0: tot_sum += 1
print(tot_sum)
