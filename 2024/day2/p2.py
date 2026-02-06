data = [list(map(int, line.split(" "))) for line in open('inp').read().split('\n')]
this_sum = 0
def check_safe(li):
    this_list = []
    for x, n in enumerate(li):
        if x != 0:
            this_list.append(n - li[x - 1])
    if (0 < min(this_list) < 4 and 0 < max(this_list) < 4) or (-4 < min(this_list) < 0 and -4 < max(this_list) < 0):
        return 1
    return 0

for l in data:
    this_list = []
    if check_safe(l):
        this_sum += 1
    else:
        for x in range(len(l)):
            copy_l = l.copy()
            copy_l.pop(x)
            if check_safe(copy_l):
                this_sum += 1
                break
print(this_sum)