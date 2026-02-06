import re
data = [int(''.join(re.findall(r'\d+', line))) for line in open('inp').read().split('\n')]
print(sum([1 if (data[0] - tm) * tm > data[1] else 0 for tm in range(data[0])]))
