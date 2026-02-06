from collections import defaultdict
data = tuple((l.split("-")[:-1], int(l.split("-")[-1].split("[")[0]), l.split("[")[1].split("]")[0]) for l in open('inp'))
tot_sum = 0
for s, i, cs in data:
    this_dict = defaultdict(int)
    for ss in s:
        for sss in ss:
            this_dict[sss] += 1
    this_check = sorted([(k, v) for k, v in this_dict.items()], key = lambda x: (-x[1], x[0]))
    this_cs = "".join([a for a, _ in this_check[:5]])
    if this_cs == cs: tot_sum += i
print(tot_sum)