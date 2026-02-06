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
                dist_diff = ant2 - ant1
                this_pos = ant1
                antinodes.add(this_pos)
                while True:
                    this_pos += dist_diff
                    if 0 <= this_pos.real < max_real and 0 <= this_pos.imag < max_imag:
                        antinodes.add(this_pos)
                    else:
                        break
                while True:
                    this_pos -= dist_diff
                    if 0 <= this_pos.real < max_real and 0 <= this_pos.imag < max_imag:
                        antinodes.add(this_pos)
                    else:
                        break
print(len(antinodes))