data = tuple(list(map(int, l.split())) for l in open('inp'))
tot_good = 0
for x in range(len(data)//3):
    for y in range(3):
        t1, t2, t3 = sorted([data[(x*3)][y], data[(x*3)+1][y], data[(x*3)+2][y]])
        tot_good += 1 if t3 < t1 + t2 else 0
print(tot_good)