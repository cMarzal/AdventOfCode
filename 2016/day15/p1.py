from math import prod

data = tuple((int(line.split()[2][:-1]), int(line.split()[4][:-1]), int(line.split()[6][:-1]), int(line.split()[8][:-1]))  for line in open('inp'))

options = set()
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - (a + b + c)
            options.add((a, b, c, d))

highest = 0
for o in options:
    tot_sum = 0
    tot_sum += prod(max(0, data[0][i]*o[0] + data[1][i]*o[1] + data[2][i]*o[2] + data[3][i]*o[3]) for i in range(4))
    highest = max(highest, tot_sum)

print(highest)