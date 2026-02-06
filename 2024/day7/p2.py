sums = [int(line.split(":")[0]) for line in open('inp').read().split('\n')]
ops = [list(map(int, line.split(": ")[1].split(" "))) for line in open('inp').read().split('\n')]
tot_sum = 0
def to_check(needed, ss, pos, array):
    if pos == len(array) - 1:
        if ss + array[pos] == needed or ss * array[pos] == needed or int(str(ss) + str(array[pos]))  == needed:
            return 1
        else:
            return 0
    else:
        if to_check(needed, ss + array[pos], pos+1, array) or to_check(needed, ss * array[pos], pos+1, array):
            return 1
        else:
            return to_check(needed, int(str(ss)+str(array[pos])), pos+1, array)

for tot, op in zip(sums,ops):
    if to_check(tot, op[0], 1, op):
        tot_sum += tot

print(tot_sum)
