import re
data = [re.findall(r'\d+', line) for line in open('inp').read().split('\n')]
total = sum([(int(d[0][0]) * 10) + int(d[-1][-1]) for d in data])

print(total)
