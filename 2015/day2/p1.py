data = tuple(sorted(list(map(int, line.split("x")))) for line in open('inp').read().split('\n'))
print(sum( 2*(d1*d2 + d1*d3 + d2*d3) + d1*d2 for d1, d2, d3 in data))
