orders = {line.split("|") for line in [sect for sect in open('inp').read().split('\n\n')][0].split('\n')}
checks = {line.split(",") for line in [sect for sect in open('inp').read().split('\n\n')][1].split('\n')}
tot_add = 0
for check in checks:
    comp = 1
    for order in orders:
        if order[0] in check and order[1] in check:
            if check.index(order[0]) > check.index(order[1]):
                comp = 0
                break
    if comp:
        tot_add += int(check[int((len(check)-1)/2)])
print(tot_add)