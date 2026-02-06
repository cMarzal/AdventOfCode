import re
pos = [list(map(int, re.findall(r'\d+', line.split()[0]))) for line in open('inp').read().split('\n')]
dirs = tuple(list(map(int, re.findall(r'-?\d+', line.split()[1]))) for line in open('inp').read().split('\n'))
for _ in range(100):
    this_pos = tuple(pos)
    for x, (p, v) in enumerate(zip(this_pos, dirs)):
        pos[x] = [(p[0]+v[0])%101,(p[1]+v[1])%103]
Q1 = len([p for p in pos if p[0]<50 and p[1]<51])
Q2 = len([p for p in pos if p[0]>50 and p[1]<51])
Q3 = len([p for p in pos if p[0]<50 and p[1]>51])
Q4 = len([p for p in pos if p[0]>50 and p[1]>51])
print(Q1*Q2*Q3*Q4)
