from collections import defaultdict
from itertools import pairwise

def f(s):
    s ^= s << 6 & 0xFFFFFF
    s ^= s >> 5 & 0xFFFFFF
    return s ^ s << 11 & 0xFFFFFF

sum2 = defaultdict(int)
for s in map(int, open('inp')):
    nums = [s] + [s := f(s) for _ in range(2000)]
    diffs = [b%10-a%10 for a,b in pairwise(nums)]
    seen = set()
    for i in range(len(nums)-4):
        pat = tuple(diffs[i:i+4])
        if pat not in seen:
            sum2[pat] += nums[i+4] % 10
            seen.add(pat)

print(max(sum2.values()))