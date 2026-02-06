ranges = [tuple(map(int, line.split("-"))) for line in open('inp').read().split('\n\n')[0].split('\n')]
ranges.sort(key=lambda x: x[0])
new_ranges = []
start, end = ranges[0]
for this_start, this_end in ranges[1:]:
    if this_start <= end + 1:
        end = max(end, this_end)
    else:
        new_ranges.append((start, end))
        start, end = this_start, this_end

new_ranges.append((start, end))

print(sum(e - s + 1 for s, e in new_ranges))
