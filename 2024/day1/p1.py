data_1 = [int(line.split("   ")[0]) for line in open('inp').read().split('\n')]
data_2 = [int(line.split("   ")[1]) for line in open('inp').read().split('\n')]
data_1.sort()
data_2.sort()
tot_sum = 0
for n1, n2 in zip(data_1, data_2):
    tot_sum += abs(n1-n2)

print(tot_sum)
