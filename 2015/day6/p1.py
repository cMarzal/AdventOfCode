import re

data = tuple(re.findall(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line)[0] for line in open('inp').read().split('\n'))
lights = set()
for what, sx, sy, ex, ey in data:
    sx, sy, ex, ey = (int(x) for x in (sx, sy, ex, ey))
    to_change = {complex(x,y) for x in range (sx,ex+1) for y in range(sy,ey+1)}
    if what == "turn off":
        lights.difference_update(to_change)
    elif what == "turn on":
        lights.update(to_change)
    else:
        lights.symmetric_difference_update(to_change)
print(len(lights))