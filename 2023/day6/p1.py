import re

data = [list(map(int, re.findall(r'\d+', line))) for line in open('inp').read().split('\n')]

total_count = 1

for x in range(len(data[0])):
    this_wins = 0
    for tm in range(data[0][x]):
        if (data[0][x] - tm) * tm > data[1][x]:
            this_wins += 1
    total_count *= this_wins

print(total_count)
