data = (tuple(map(int, line.split("-"))) for line in open('inp').read().split(','))
this_sum = 0
for d1, d2 in data:
    for d in range(d1,d2+1):
        if len(str(d))%2 == 0:
            if str(d)[int(len(str(d))/2):] == str(d)[:int(len(str(d))/2)]: this_sum += d
print(this_sum)