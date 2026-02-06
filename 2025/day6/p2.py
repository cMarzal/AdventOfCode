from math import prod

nums = [list(map(int, line.split())) for line in open('inp').readlines()[:-1]]
nums_str = [line for line in open('inp').readlines()[:-1]]
ops = open('inp').readlines()[-1].split()
tot_sum = 0
max_pos = 0
for x in range(len(nums[0])):
    n_tot = []
    max_l = max([len(str(n[x])) for n in nums])
    pp = [ns.find(str(nn[x]),max_pos) for ns, nn in zip(nums_str, nums)]
    max_pos += max_l + 1
    for y in range(max_l):
        if max(pp) == min(pp):
            new_num = "".join([str(nn[x])[y] for nn in nums if len(str(nn[x])) > y])
        else:
            new_num = "".join([str(nn[x])[len(str(nn[x])) - max_l + y] for nn in nums if max_l - y <= len(str(nn[x]))])
        n_tot.append(int(new_num))
    tot_sum += sum(n_tot) if ops[x] == "+" else prod(n_tot)
print(tot_sum)
