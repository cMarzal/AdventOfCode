data_blocks = [int(n) for line in open('inp').read().split('\n') for x, n in enumerate(line) if x%2==0]
data_spaces = [int(n) for line in open('inp').read().split('\n') for x, n in enumerate(line) if x%2==1]
this_pos = 0
max_pos = len(data_blocks)-1
spaces_done = 0
all_array = []
while True:
    if max_pos == this_pos:
        for _ in range(data_blocks[this_pos] - spaces_done):
            all_array.append(this_pos)
        break
    for _ in range(data_blocks[this_pos]):
        all_array.append(this_pos)
    for _ in range(data_spaces[this_pos]):
        if data_blocks[max_pos] > spaces_done:
            all_array.append(max_pos)
            spaces_done += 1
        else:
            max_pos -= 1
            if max_pos == this_pos:
                break
            else:
                spaces_done = 1
                all_array.append(max_pos)
    this_pos += 1
print(sum([order * number for order, number in enumerate(all_array)]))
