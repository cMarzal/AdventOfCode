data = ((line.split(" ")[0], int(line.split(" ")[1]), line.split(" ")[2]) for line in open('inp').read().split('\n'))

dirs = {"U": -1j, "D": 1j, "R": 1, "L": -1}
this_x = 0
total_covered = 1
for dir, num, _ in data:
    this_x += num * dirs[dir].real
    total_covered += dirs[dir].imag * num * this_x + num/2

print(int(total_covered))