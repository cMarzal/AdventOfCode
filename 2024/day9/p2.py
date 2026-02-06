data_blocks = [int(n) for line in open('inp').read().split('\n') for x, n in enumerate(line) if x%2==0]
data_spaces = [int(n) for line in open('inp').read().split('\n') for x, n in enumerate(line) if x%2==1]
this_pos = 0
max_pos = len(data_spaces)
pos_done = set()
all_array = []
while True:
    if this_pos >= max_pos:
        break
    if this_pos not in pos_done:
        for _ in range(data_blocks[this_pos]):
            all_array.append(this_pos)
    else:
        for _ in range(data_blocks[this_pos]):
            all_array.append(".")
    this_spaces = data_spaces[this_pos]
    for i in range(max_pos, this_pos, -1):
        if i not in pos_done and data_blocks[i] <= this_spaces:
            for _ in range(data_blocks[i]):
                all_array.append(i)
            pos_done.add(i)
            max_num = max({j for j in range(len(data_spaces))} - pos_done)
            this_spaces -= data_blocks[i]
            if this_spaces == 0:
                break
    for _ in range(this_spaces):
        all_array.append(".")
    this_pos += 1

print(sum([order * number for order, number in enumerate(all_array) if number != "."]))
