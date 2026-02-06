import itertools

data = {frozenset([line.split()[0],line.split()[2]]): int(line.split()[4]) for line in open('inp')}
cities = {city for pair in data.keys() for city in pair}
all_orders = set(itertools.permutations(cities))
tot_sum = 0
for cc in all_orders:
    tot_sum = max(tot_sum, sum(data[frozenset([c1, c2])] for  c1, c2 in zip(cc,cc[1:])))
print(tot_sum)