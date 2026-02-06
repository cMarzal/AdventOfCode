from itertools import combinations

data = [(int(line.split(",")[0]),int(line.split(",")[1])) for line in open('inp').read().split('\n')]
pairs = combinations(data, 2)
distances = sorted([(abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1) for p1, p2 in pairs])
print(distances[-1])
