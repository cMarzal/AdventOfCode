import re
data = [[list(map(int, re.findall(r'\d+', line2))) for line2 in line.split("\n")] for line in open('inp').read().split('\n\n')]

seeds_1 = data[0][0]
this_map = []

for num in range(len(seeds_1)):
    if num%2 == 1:
        this_map.append((seeds_1[num-1], seeds_1[num] + seeds_1[num-1] -1))

for x, sect in enumerate(data):
    new_map = []
    this_done = [0 for _ in range(len(this_map))]
    check_map = []
    if x != 0:
        for line in sect:
            if len(line) == 3:
                for y, seed_range in enumerate(this_map):
                    if seed_range[0] <= line[1] <= seed_range[1] <= line[1] + line[2] - 1:
                        new_map.append([line[0], seed_range[1] - line[1] + line[0]])
                        this_done[y] = 1
                        check_map.append([seed_range[0], line[1]-1])
                    elif seed_range[0] <= line[1] and line[1] + line[2] -1 <= seed_range[1]:
                        new_map.append([line[0], line[2] + line[0] -1])
                        this_done[y] = 1
                        check_map.append([seed_range[0], line[1]-1])
                        check_map.append([line[1] + line[2], seed_range[1]])
                    elif line[1] <= seed_range[0] <= line[1] + line[2] -1 <= seed_range[1]:
                        new_map.append([seed_range[0] - line[1] + line[0], line[2] + line[0] -1])
                        this_done[y] = 1
                        check_map.append([line[1] + line[2], seed_range[1]])
                    elif line[1] <= seed_range[0] <= seed_range[1] <= line[1] + line[2] -1 :
                        new_map.append([seed_range[0] - line[1] + line[0], seed_range[1] - line[1] + line[0]])
                        this_done[y] = 1
        for n, xx in enumerate(this_done):
            if xx == 0:
                new_map.append(this_map[n])
        this_map = new_map.copy()

print(min([x[0] for x in this_map]))
