data = (sorted(list(map(int, l.split()))) for l in open('inp'))
print(sum(1 for t1, t2, t3 in data if t3 < t1 + t2))
