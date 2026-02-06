l1, *data = open('inp')
this_rays = {l1.index("S")}
tot_splits = 0
for line in data:
    new_rays = set()
    for r in this_rays:
        if line[r] == "^":
            new_rays.update({r-1,r+1})
            tot_splits += 1
        else:
            new_rays.add(r)
    this_rays = new_rays
print(tot_splits)
