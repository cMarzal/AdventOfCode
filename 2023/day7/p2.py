import re
data = [list(map(int, re.findall(r'\d+', line))) for line in open('inp').read().split('\n')]
