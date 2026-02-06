import re
data = [[re.findall(r'\d+', line.split(":")[1].split("|")[0]), re.findall(r'\d+', line.split(":")[1].split("|")[1])] for line in open('inp').read().split('\n')]
nums = [1 for x in range(len(data))]
for y, [t1, t2] in enumerate(data):
    nn = 1
    for x in t2:
        if x in t1:
            nums[y+nn] += nums[y]
            nn += 1
print(sum(nums))