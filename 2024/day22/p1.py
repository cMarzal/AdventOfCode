def f(s):
    s ^= s << 6 & 0xFFFFFF
    s ^= s >> 5 & 0xFFFFFF
    return s ^ s << 11 & 0xFFFFFF

ss = 0
for s in map(int, open("inp")):
    nums = [s] + [s := f(s) for _ in range(2000)]
    ss += nums[-1]

print(ss)