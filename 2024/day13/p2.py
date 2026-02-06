import re
data = tuple(tuple(tuple(int(n) for n in re.findall(r'\d+', line)) for line in chunk.split('\n') if line) for chunk in open('inp').read().split('\n\n'))
total_sum = 0
for g in data:
    price_x = g[2][0] + 10000000000000
    price_y = g[2][1] + 10000000000000
    but_A = (price_x*g[1][1] - price_y*g[1][0]) / (g[0][0]*g[1][1] - g[0][1]*g[1][0])
    but_B = (price_y*g[0][0] - price_x*g[0][1]) / (g[0][0]*g[1][1] - g[0][1]*g[1][0])
    if but_A == int(but_A) and but_B == int(but_B):
        total_sum += int(but_A*3 + but_B)
print(total_sum)

