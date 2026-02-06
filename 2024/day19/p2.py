from functools import cache

data = tuple(group for group in open('inp').read().split('\n\n'))
at = tuple(data[0].split(", "))
pt = data[1].split("\n")

@cache
def check_strs(s):
    sum = 0
    check = set(a for a in at if s.startswith(a))
    for t in check:
        if s == t:
            sum += 1
        ss = s[len(t):]
        sum += check_strs(ss)
    return sum

possible = 0
for p in pt:
    possible += check_strs(p)

print(possible)