data = [line for line in open('inp').read().split('\n')]
all_antennas = dict()
antinodes = set()
max_real = len(data[0])
max_imag = len(data)
for x, l in enumerate(data):
    for y, c in enumerate(l):
        if c != ".":
            all_antennas.setdefault(c, []).append(complex(y, x))
for v in all_antennas.values():
    for ant1 in v:
        for ant2 in v:
            if ant1 != ant2:
                antinode1 = ant2 + ant2 - ant1
                antinode2 = ant1 + ant1 - ant2
                if 0 <= antinode1.real < max_real and 0 <= antinode1.imag < max_imag:
                    antinodes.add(antinode1)
                if 0 <= antinode2.real < max_real and 0 <= antinode2.imag < max_imag:
                    antinodes.add(antinode2)
print(len(antinodes))