from collections import defaultdict

data = {group.split(": ")[0]: set(group.split(": ")[1].split())  for group in open('inp').read().split('\n')}

cons = defaultdict(set)
cons.update(data)

for k, v in data.items():
    for comp in v:
        if k not in cons[comp]:
            new_set = cons[comp]
            new_set.add(k)

s = set(cons)
count = lambda v: len(cons[v]-s)

while sum(map(count, s)) != 3:
    s.remove(max(s, key=count))
print(len(s) * len(set(cons)-s))