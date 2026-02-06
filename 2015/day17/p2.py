data = [int(line) for line in open('inp')]

def find_sample(this_s, this_v, size):
    new_s = this_s.copy()
    size += 1
    sizes = []
    while new_s:
        s = new_s.pop(0)
        new_v = this_v
        if this_v + s == 150:
            sizes.append(size)
        elif new_s and this_v + s <= (150-min(new_s)):
            sizes.extend(find_sample(new_s, new_v + s, size))
    return sizes
this_samples = find_sample(data, 0, 0)
print(this_samples.count(min(this_samples)))