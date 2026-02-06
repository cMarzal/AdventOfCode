from re import findall

data = (tuple(map(int, line.split("-"))) for line in open('inp').read().split(','))
this_sum = 0
for d1, d2 in data:
    for d in range(d1,d2+1):
        if findall(r'^(\d+)\1+$', str(d)): this_sum += d
print(this_sum)