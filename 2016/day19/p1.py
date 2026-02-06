from collections import defaultdict

*data, _, inp = open('inp')
options = defaultdict(set)
outs = set()
for line in data:
    options[line.split()[0]].add(line.split()[2])
for i, l in enumerate(inp):
    for l2 in options[l]:
        outs.add(inp[:i] + l2 + inp[i + 1:])
    if i > 0:
        for l2 in options[inp[i-1] + l]:
            outs.add(inp[:i-1] + l2 + inp[i + 1:])

print(len(outs))