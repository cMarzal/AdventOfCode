from functools import cache

data = tuple(group for group in open('inp').read().split('\n\n'))
at = tuple(data[0].split(", "))
pt = data[1].split("\n")

@cache
def check_strs(s):
    check = set(a for a in at if s.startswith(a))
    for t in check:
        if s == t:
            return 1
        ss = s[len(t):]
        if check_strs(ss) == 1:
            return 1
    return 0

possible = 0
for p in pt:
    possible += check_strs(p)

print(possible)