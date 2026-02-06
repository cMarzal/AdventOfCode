data = [list(map(int, line.split(" "))) for line in open('inp').read().split('\n')]
def calc_road(this_road):
    new_road = []
    for x, num in enumerate(this_road):
        if x != 0:
            new_road.append(num - this_road[x-1])
    return new_road
total_count = 0
for row in data:
    this_num = 0
    calc_row = row.copy()
    while True:
        this_num += calc_row[-1]
        calc_row = calc_road(calc_row)
        if calc_row.count(0) == len(calc_row) or calc_row == []:
            break
    total_count += this_num
print(total_count)