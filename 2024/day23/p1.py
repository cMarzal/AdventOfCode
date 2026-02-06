from collections import defaultdict
from itertools import combinations

data = (group.split('-') for group in open('inp').read().split('\n'))

conn = defaultdict(set)

for a, b in data:
    conn[a].add(b)
    conn[b].add(a)
triangles = set()

for node in conn:
    for n1, n2 in combinations(conn[node], 2):
        if n2 in conn[n1]:
            triangle = tuple(sorted([node, n1, n2]))
            triangles.add(triangle)

start_t = []
for link in triangles:
    for l in link:
        if l.startswith("t"):
            start_t.append(link)
            break
print(len(start_t))
