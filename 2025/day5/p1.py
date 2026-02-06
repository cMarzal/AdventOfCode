ranges = {tuple(map(int, line.split("-"))) for line in open('inp').read().split('\n\n')[0].split('\n')}
checks = set(int(line) for line in open('inp').read().split('\n\n')[1].split('\n'))
tot_add = 0
for check in checks:
    for r in ranges:
        if r[0] <= check <= r[1]:
            tot_add += 1
            break

print(tot_add)