data = [group.split('\n') for group in open('inp').read().split('\n\n')]
total_sum = 0
for pattern in data:
    for x in range(1, len(pattern)):
        if pattern[:x][::-1][:min(x, len(pattern)-x)] == pattern[x:][:min(x, len(pattern)-x)]:
            total_sum += (100*x)
    tr_pattern = [[row[i] for row in pattern] for i in range(len(pattern[0]))]
    for y in range(1, len(tr_pattern)):
        if tr_pattern[:y][::-1][:min(y, len(tr_pattern)-y)] == tr_pattern[y:][:min(y, len(tr_pattern)-y)]:
            total_sum += y
print(total_sum)
