import re
import matplotlib.pyplot as plt
import numpy as np
pos = [tuple(map(int, re.findall(r'\d+', line.split()[0]))) for line in open('inp').read().split('\n')]
dirs = tuple(list(map(int, re.findall(r'-?\d+', line.split()[1]))) for line in open('inp').read().split('\n'))
this_secs = 0
while True:
    this_pos = tuple(pos)
    for x, (p, v) in enumerate(zip(this_pos, dirs)):
        pos[x] = tuple([(p[0]+v[0])%101,(p[1]+v[1])%103])
    this_secs += 1
    if len(set(pos)) == len(pos):
        break

points = np.array(pos)

img = np.zeros((103, 103))

for x, y in points:
    img[y, x] = 1

plt.imshow(img, cmap="gray", origin="upper")  # Use 'gray' colormap
plt.grid(False)
plt.show()
print(this_secs)