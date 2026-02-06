data = [int(line) for line in open('inp')]

def find_sample(this_s, this_v):
    tot = 0
    new_s = this_s.copy()
    while new_s:
        s = new_s.pop(0)
        new_v = this_v
        if this_v + s == 150:
            tot += 1
        elif new_s and this_v + s <= (150-min(new_s)):
            tot += find_sample(new_s, new_v + s)
    return tot
print(find_sample(data, 0))