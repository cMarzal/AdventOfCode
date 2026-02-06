import re
data = tuple(tuple(tuple(int(n) for n in re.findall(r'\d+', line)) for line in chunk.split('\n') if line) for chunk in open('inp').read().split('\n\n'))
total_sum = 0
for g in data:
    min_option = 999999999
    price_x = g[2][0]
    price_y = g[2][1]
    for n in range(min(int(price_x/g[0][0]),int(price_y/g[0][1]))+1):
        rem_x = price_x - (g[0][0]*n)
        rem_y = price_y - (g[0][1]*n)
        if rem_x%g[1][0] == 0 and rem_x/g[1][0] == rem_y/g[1][1]:
            min_option = min(min_option, int(n*3 + rem_x/g[1][0]))
            break
    total_sum += min_option if min_option != 999999999 else 0
print(total_sum)
