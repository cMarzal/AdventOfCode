data = [list(map(int, list(line))) for line in open('inp').read().split('\n')]
print(sum([int(str(max(d[:-1])) + str(max(d[d.index(max(d[:-1]))+1:]))) for d in data]))
