import regex as re

data = ["".join(re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine', line, overlapped = True)) for line in open('inp').read().split('\n')]
dd = dict()
dd["one"] = 1
dd["two"] = 2
dd["three"] = 3
dd["four"] = 4
dd["five"] = 5
dd["six"] = 6
dd["seven"] = 7
dd["eight"] = 8
dd["nine"] = 9
for k, v in dd.items():
    data = [d.replace(k, str(v)) for d in data]
total = sum([(int(d[0]) * 10) + int(d[-1]) for d in data])
print(total)
