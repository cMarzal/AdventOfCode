data = [list(map(int, line.split(" "))) for line in open('inp').read().split('\n')]
this_sum = 0
for l in data:
    this_list = []
    for x, n in enumerate(l):
        if x != 0:
            this_list.append(n-l[x-1])
    if (0 < min(this_list) < 4 and 0 < max(this_list) < 4) or (-4 < min(this_list) < 0 and -4 < max(this_list) < 0):
        this_sum += 1
print(this_sum)