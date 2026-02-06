data = tuple(sorted(list(map(int, line.split("x")))) for line in open('inp').read().split('\n'))
print(sum( (d1*d2*d3) + 2*(d1+d2) for d1, d2, d3 in data))
