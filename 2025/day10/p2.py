import pulp

data = [(line.split("{")[1].split("}")[0], line.split("] ")[1].split(" {")[0].replace("(","").replace(")","").split()) for line in open('inp').read().split('\n')]
order = tuple(list(map(int, l.split(","))) for l, _ in data)
switches = tuple(sorted([set(map(int, nums.split(","))) for nums in s], key=lambda x: len(x),reverse=True) for _, s in data)
tot_mov = 0

def min_presses(buttons, target):
    M = len(buttons)
    N = len(target)
    model = pulp.LpProblem("button_press_minimization", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(M)]
    model += pulp.lpSum(x)
    for i in range(N):
        model += pulp.lpSum(x[j] for j in range(M) if i in buttons[j]) == target[i]
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    return int(sum(v.value() for v in x))

for o, s in zip(order,switches):
    tot_mov += min_presses(s, o)
print(tot_mov)