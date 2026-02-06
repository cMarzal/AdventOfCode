galaxy = [line for line in open('inp').read().split('\n')]
temp_galaxy = galaxy.copy()
new_galaxy = []
for x in range(len(galaxy[0])):
    if all(line[x] == "." for line in galaxy):
        for y in range(len(galaxy)):
            temp_galaxy[y] = temp_galaxy[y][:x] + "X" + temp_galaxy[y][x+1:]
for x, line in enumerate(temp_galaxy):
    if all(space in [".","X"] for space in line):
        new_line = line.replace(".", "X")
        new_galaxy.append(new_line)
    else:
        new_galaxy.append(line)

galaxies = [(x,y) for y,line in enumerate(new_galaxy) for x,space in enumerate(line) if space == "#"]
total_dist = 0
for n,g1 in enumerate(galaxies):
    for m,g2 in enumerate(galaxies):
        if m>n:
            for d1 in range(abs(g2[0]-g1[0])):
                if new_galaxy[g1[1]][max(g2[0],g1[0])-d1-1] == "X":
                    total_dist += 1000000
                else:
                    total_dist += 1
            for d2 in range(abs(g2[1]-g1[1])):
                if new_galaxy[max(g2[1],g1[1])-d2-1][g1[0]] == "X":
                    total_dist += 1000000
                else:
                    total_dist += 1
print(total_dist)