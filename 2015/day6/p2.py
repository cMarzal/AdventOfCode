import re

data = tuple(re.findall(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line)[0] for line in open('inp').read().split('\n'))
lights = {complex(x,y): 0 for x in range (1000) for y in range(1000)}
for what, sx, sy, ex, ey in data:
    sx, sy, ex, ey = (int(x) for x in (sx, sy, ex, ey))
    to_change = {complex(x,y) for x in range (sx,ex+1) for y in range(sy,ey+1)}
    if what == "turn off":
        for tc in to_change:
            lights[tc] = max(lights[tc]-1,0)
    elif what == "turn on":
        for tc in to_change:
            lights[tc] += 1
    else:
        for tc in to_change:
            lights[tc] += 2
print(sum(x for x in lights.values()))