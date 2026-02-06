data = [group.split('\n') for group in open('inp').read().split('\n\n')]
total_sum = 0
for pattern in data:
    for x in range(1, len(pattern)):
        size = min(x, len(pattern)-x)
        comp1 = pattern[:x][::-1][:size]
        comp2 = pattern[x:][:size]
        total_same = sum([1 if comp1[m][n] == comp2[m][n] else 0 for m in range(len(comp1)) for n in range(len(comp1[0]))])
        if total_same + 1 == len(comp1) * len(comp1[0]):
            total_sum += (100*x)
    tr_pattern = [[row[i] for row in pattern] for i in range(len(pattern[0]))]
    for y in range(1, len(tr_pattern)):
        size = min(y, len(tr_pattern) - y)
        comp1 = tr_pattern[:y][::-1][:size]
        comp2 = tr_pattern[y:][:size]
        total_same = sum([1 if comp1[m][n] == comp2[m][n] else 0 for m in range(len(comp1)) for n in range(len(comp1[0]))])
        if total_same + 1 == (len(comp1) * len(comp1[0])):
            total_sum += y
print(total_sum)
