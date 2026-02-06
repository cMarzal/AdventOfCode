from collections import defaultdict
data = tuple(l for l in open('inp').read().split("\n"))
st = ""
for x in range(len(data[0])):
    this_d = defaultdict(int)
    for d in data:
        this_d[d[x]] += 1
    st += min(this_d, key=this_d.get)
print(st)
