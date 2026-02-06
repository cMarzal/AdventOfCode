data = {line for line in open('inp').read().split('\n')}
vowel = {"a", "e", "i", "o", "u"}
proh = {"ab", "cd", "pq", "xy"}
tot = 0
for d in data:
    if sum(d.count(p) for p in proh) == 0:
        if sum(d.count(v) for v in vowel) >= 3:
            for x, s in enumerate(d[:-1]):
                if s == d[x+1]:
                    tot += 1
                    break
print(tot)
