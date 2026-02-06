galaxy = [line for line in open('inp').read().split('\n')]
temp_galaxy = galaxy.copy()
new_galaxy = []
to_add = 1
for x in range(len(galaxy[0])):
    if all(line[x] == "." for line in galaxy):
        for y in range(len(galaxy)):
            temp_galaxy[y] = temp_galaxy[y][:x+to_add] + "." + temp_galaxy[y][x+to_add:]
        to_add += 1
for x, line in enumerate(temp_galaxy):
    if all(space == "." for space in line):
        new_galaxy.append(line)
        new_galaxy.append(line)
    else:
        new_galaxy.append(line)

galaxies = [(x,y) for y,line in enumerate(new_galaxy) for x,space in enumerate(line) if space == "#"]
total_dist = 0
for n,g1 in enumerate(galaxies):
    for m,g2 in enumerate(galaxies):
        if m>n:
            total_dist += abs(g2[0]-g1[0]) + abs(g2[1]-g1[1])
print(total_dist)