data = [(line.split("[")[1].split("]")[0], line.split("] ")[1].split(" {")[0].replace("(","").replace(")","").split()) for line in open('inp').read().split('\n')]
order = tuple({idx for idx, ch in enumerate(l) if ch == '#'} for l, _ in data)
switches = tuple([set(map(int, nums.split(","))) for nums in s] for _, s in data)
tot_mov = 0

def check_min(orde, sw, curr, moves, min_moves):
    if moves < min_moves:
        sw2 = sw.copy()
        moves += 1
        while sw2:
            ss = sw2.pop(0)
            if curr != ss:
                this_s = curr.copy()
                this_s.symmetric_difference_update(ss)
                if this_s == orde:
                    min_moves =moves
                    break
                else:
                    min_moves = min(min_moves, check_min(orde, sw2, this_s, moves, min_moves))
    return min_moves

for o, s in zip(order,switches):
    tot_mov += check_min(o, s, set(), 0, 999)
print(tot_mov)
