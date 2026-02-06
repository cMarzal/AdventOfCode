from collections import defaultdict

data = {complex(i, j) for i,line in enumerate(open('inp').read().split('\n')) for j in range(len(line)) if line[j] == "#"}
data.update({0j,99+0j,99j,99+99j})
arr = {1, -1, 1j, -1j, 1+1j, -1+1j, 1-1j, -1-1j}
tot = 0
for _ in range(100):
    new_data = set()
    neighbors = defaultdict(int)
    for d in data:
        for a in arr:
            this_num = a+d
            if 0 <= this_num.real < 100 and 0 <= this_num.imag < 100:
                neighbors[a+d] += 1
    for k, v in neighbors.items():
        if v == 3 or (v== 2 and k in data):
            new_data.add(k)
    data = new_data
    data.update({0j, 99 + 0j, 99j, 99 + 99j})

print(len(data))