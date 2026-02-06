import re
data = [line for line in open('inp').read().split('\n')]
tot = 0
for y, line in enumerate(data):
    for x, n in enumerate(line):
        if n == "*":
            tn = []
            if y != 0:
                for num in re.finditer(r'\d+', data[y-1]):
                    if num.start(0) <= x + 1 and num.end(0) - 1 >= x - 1:
                        tn.append(num.group())
            for num in re.finditer(r'\d+', data[y]):
                if num.start(0) <= x + 1 and num.end(0) - 1 >= x - 1:
                    tn.append(num.group())
            if y != len(data):
                for num in re.finditer(r'\d+', data[y+1]):
                    if num.start(0) <= x + 1 and num.end(0) - 1 >= x - 1:
                        tn.append(num.group())
            if len(tn) == 2:
                tot += int(tn[0]) * int(tn[1])

print(tot)