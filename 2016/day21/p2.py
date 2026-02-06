info_him = [int(line.split(": ")[1]) for line in open('inp')]
wea = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
arm = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rin = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

possible_l = set()
for i in reversed(range(4,11)):
    for j in reversed(range(6)):
        stop = 0
        info_you = [100, i, j]
        life_you = 100
        life_him = info_him[0]
        while True:
            life_him -= max(info_you[1]-info_him[2],1)
            if life_him <= 0: break
            life_you -= max(info_him[1] - info_you[2], 1)
            if life_you <= 0:
                possible_l.add((i, j))
                stop=1
                break
        if stop: break
max_cost = 0
for a, d in possible_l:
    cost_a = wea[a-4][0] if a <= 8 else 0
    cost_d = arm[d-1][0] if 1 <= d <= 4 else 0
    for p1, a1, _ in wea:
        if 0 <= a-a1-1 < 3:
            cost_a = max(cost_a, p1+rin[a-a1-1][0])
    for p1, _, d1 in arm:
        if 0 <= d-d1-1 < 3:
            cost_d = max(cost_d, p1+rin[d-d1+2][0])
    cost = cost_d + cost_a
    max_cost = max(max_cost, cost_d + cost_a)

print(possible_l)
print(max_cost)