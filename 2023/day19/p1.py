data = tuple(group for group in open('inp').read().split('\n\n'))
path = {l.split('{')[0]: (l.split('{')[1].split(',')[:-1], l.split('{')[1].split(',')[-1][:-1]) for l in
        data[0].split('\n')}
inputs = tuple({item.split("=")[0]: int(item.split("=")[1]) for item in line.strip('{}').split(",")} for line in
               data[1].split('\n'))

def check_inp(inp, mats):
    for c in path[inp][0]:
        if eval(c.split(":")[0].replace(c.split(":")[0][0], str(mats[c.split(":")[0][0]]))):
            res = c.split(":")[1]
            break
    else:
        res = path[inp][1]
    return sum(v for v in mats.values()) if res == "A" else 0 if res == "R" else check_inp(res, mats)

print(sum(check_inp("in", m) for m in inputs))
