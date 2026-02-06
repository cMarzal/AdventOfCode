import re
data = [[list(map(int, re.findall(r'\d+', line2))) for line2 in line.split("\n")] for line in open('inp').read().split('\n\n')]
seeds = data[0][0]
new_seeds = seeds.copy()

for x, sect in enumerate(data):
    if x != 0:
        for line in sect:
            if len(line) == 3:
                for y, seed in enumerate(seeds):
                    if line[1] <= seed < line[1] + line[2]:
                        new_seeds[y] = seed - line[1] + line[0]
    seeds = new_seeds.copy()
print(min(seeds))
