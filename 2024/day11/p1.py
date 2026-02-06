from functools import cache
stones = [line.split(" ") for line in open('inp').read().split('\n')][0]
stones_dict = {k: 1 for k in stones}

@cache
def count_stones(x):
    ns = []
    if x == "0":
        ns.append("1")
    elif len(x) % 2 == 0:
        ns.append(str(int(x[:int(len(x) / 2)])))
        ns.append(str(int(x[int(len(x) / 2):])))
    else:
        ns.append(str(int(x) * 2024))
    return ns

for _ in range(25):
    this_stones = dict(stones_dict)
    for stone, count in this_stones.items():
        add_stones = count_stones(stone)
        stones_dict[stone] -= count
        for s in add_stones:
            try:
                stones_dict[s] += count
            except:
                stones_dict[s] = count

print(sum([cc for cc in stones_dict.values()]))