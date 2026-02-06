from math import prod

nums = [list(map(int, line.split())) for line in open('inp').readlines()[:-1]]
ops = open('inp').readlines()[-1].split()
tot_sum = 0
for x in range(len(nums[0])):
    ns = [nn[x] for nn in nums]
    tot_sum += sum(ns) if ops[x] == "+" else prod(ns)
print(tot_sum)
