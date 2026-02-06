data = ((line.split(" ")[0], int(line.split(" ")[1]), line.split(" ")[2]) for line in open('inp').read().split('\n'))

dirs = {"3": -1j, "1": 1j, "0": 1, "2": -1}
this_x = 0
total_covered = 1
for _, _, x in data:
    dir = dirs[x[7]]
    num = int(x[2:7], 16)
    this_x += num * dir.real
    total_covered += dir.imag * num * this_x + num/2

print(int(total_covered))