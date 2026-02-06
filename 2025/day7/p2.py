from collections import defaultdict

l1, *data = open('inp')
this_rays = defaultdict(int)
this_rays[l1.index("S")] = 1
for line in data:
    new_rays = defaultdict(int)
    for k, v in this_rays.items():
        if line[k] == "^":
            new_rays[k-1] += v
            new_rays[k+1] += v
        else:
            new_rays[k] += v
    this_rays = new_rays
print(sum([i for i in this_rays.values()]))
