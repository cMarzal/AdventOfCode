import re
data = [line for line in open('inp').read().split('\n')]

data_nn = [re.sub(r'\d', ".", line) for line in data]
ss = 0
for y, line in enumerate(data):
    for x in re.finditer(r'\d+', line):
        mi = max(0, x.start(0) - 1)
        ma = min(len(line), x.end(0) + 1)
        for n in range(mi, ma):
            if data_nn[y][n] != "." or data_nn[max(0, y - 1)][n] != "." or data_nn[min(y + 1, len(data_nn)-1)][n] != ".":
                ss += int(x.group())
                break
print(ss)