orders = [line.split("|") for line in [sect for sect in open('inp').read().split('\n\n')][0].split('\n')]
checks = [line.split(",") for line in [sect for sect in open('inp').read().split('\n\n')][1].split('\n')]
tot_add = 0
def check_cycle(l1,ords):
    this_check = 0
    for ord in ords:
        if l1.index(ord[0]) > l1.index(ord[1]):
            this_check = 1
            l1.pop(l1.index(ord[0]))
            l1.insert(l1.index(ord[1]), ord[0])
    if this_check:
        return check_cycle(l1,ords)
    return int(l1[int((len(l1)-1)/2)])

for check in checks:
    this_ords = []
    to_check = 0
    for order in orders:
        if order[0] in check and order[1] in check:
            this_ords.append(order)
            if check.index(order[0]) > check.index(order[1]):
                to_check = 1
                check.pop(check.index(order[0]))
                check.insert(check.index(order[1]),order[0])
    if to_check:
        tot_add += check_cycle(check, this_ords)
print(tot_add)