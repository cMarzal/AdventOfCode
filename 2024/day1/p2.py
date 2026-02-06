data_1 = [int(line.split("   ")[0]) for line in open('inp').read().split('\n')]
data_2 = [int(line.split("   ")[1]) for line in open('inp').read().split('\n')]
tot_sum = 0
for n1 in data_1:
    tot_sum += data_2.count(n1) * n1
print(tot_sum)